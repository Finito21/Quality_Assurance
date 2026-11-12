"""Tests for hooks/typography.py (run with: python -m unittest discover -s tests)."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "hooks"))

from types import SimpleNamespace  # noqa: E402

from typography import NBSP, fix_typography, on_page_content  # noqa: E402


def fix(text: str) -> str:
    """Run the hook and show non-breaking spaces as '~' for readable asserts."""
    return fix_typography(text).replace(NBSP, "~")


class OneLetterWords(unittest.TestCase):
    def test_single_letter_words_are_glued(self):
        self.assertEqual(fix("Testy w domu i w pracy"), "Testy w~domu i~w~pracy")

    def test_uppercase_single_letter(self):
        self.assertEqual(fix("A teraz"), "A~teraz")

    def test_before_inline_tag(self):
        self.assertEqual(fix('opisane w <a href="x">Dokumentacji</a>'), 'opisane w~<a href="x">Dokumentacji</a>')

    def test_after_line_break_tag(self):
        self.assertEqual(fix("x<br/>w domu"), "x<br/>w~domu")

    def test_letters_inside_words_untouched(self):
        self.assertEqual(fix("kawa i herbata"), "kawa i~herbata")


class Abbreviations(unittest.TestCase):
    def test_with_full_stop(self):
        self.assertEqual(fix("np. Postman, tj. narzędzie"), "np.~Postman, tj.~narzędzie")

    def test_without_full_stop(self):
        self.assertEqual(fix("Wg słownika"), "Wg~słownika")

    def test_capitalised_and_figure_abbreviations(self):
        self.assertEqual(fix("Dr. Nowak, Rys. 1, zob. tabelę, wg. ISTQB"), "Dr.~Nowak, Rys.~1, zob.~tabelę, wg.~ISTQB")

    def test_before_inline_code(self):
        self.assertEqual(fix("np. <code>200</code>"), "np.~<code>200</code>")
        self.assertEqual(fix("wg <strong>ISTQB</strong>"), "wg~<strong>ISTQB</strong>")

    def test_not_glued_before_block_tag(self):
        self.assertEqual(fix("np.\n<ul>"), "np.\n<ul>")


class Numbers(unittest.TestCase):
    def test_number_and_unit(self):
        self.assertEqual(fix("500 ms"), "500~ms")

    def test_number_and_word(self):
        self.assertEqual(fix("1000 użytkowników"), "1000~użytkowników")

    def test_relation_sign_and_number(self):
        self.assertEqual(fix("czas &lt; 500 ms"), "czas &lt;~500~ms")
        self.assertEqual(fix("≤ 500"), "≤~500")

    def test_number_before_inline_tag(self):
        self.assertEqual(fix("500 <strong>ms</strong>"), "500~<strong>ms</strong>")
        self.assertEqual(fix("czas &lt; <code>5</code>"), "czas &lt;~<code>5</code>")

    def test_section_sign(self):
        self.assertEqual(fix("§ 5"), "§~5")

    def test_windows_line_endings(self):
        self.assertEqual(fix("tak\r\nb i\r\nc"), "tak\r\nb i~c")


class Dashes(unittest.TestCase):
    def test_dash_does_not_start_a_line(self):
        self.assertEqual(fix("tekst – dalej"), "tekst~– dalej")


class SkippedContent(unittest.TestCase):
    def test_code_is_untouched(self):
        self.assertEqual(fix("<code>a = b i c</code>"), "<code>a = b i c</code>")

    def test_pre_and_nested_code_are_untouched(self):
        html = '<pre class="mermaid"><code>A --> B i C</code></pre> i koniec'
        self.assertEqual(fix(html), '<pre class="mermaid"><code>A --> B i C</code></pre> i~koniec')

    def test_kbd_is_untouched(self):
        self.assertEqual(fix("<kbd>I</kbd> (macOS)"), "<kbd>I</kbd> (macOS)")

    def test_attributes_are_untouched(self):
        html = '<img alt="w domu i w pracy" src="x.png">'
        self.assertEqual(fix(html), html)

    def test_greater_than_inside_attribute(self):
        html = '<a title="x > a i b">link</a>'
        self.assertEqual(fix(html), html)

    def test_comment_with_greater_than(self):
        self.assertEqual(fix("<!-- a > w domu --> w domu"), "<!-- a > w domu --> w~domu")


class MarkupEdgeCases(unittest.TestCase):
    def test_html_comment_is_untouched(self):
        self.assertEqual(fix("<!-- w domu i w pracy --> w domu"), "<!-- w domu i w pracy --> w~domu")

    def test_entity_before_word_is_untouched(self):
        self.assertEqual(fix("Dev &amp; QA w domu"), "Dev &amp; QA w~domu")

    def test_unbalanced_closing_tag_does_not_disable_the_hook(self):
        self.assertEqual(fix("</code> w domu"), "</code> w~domu")

    def test_idempotent(self):
        once = fix_typography("np. 5 kg w domu – tak")
        self.assertEqual(fix_typography(once), once)

    def test_nbsp_is_a_real_non_breaking_space(self):
        self.assertEqual(NBSP, " ")


class PageLanguage(unittest.TestCase):
    CONFIG = {"theme": {"language": "pl"}}

    def run_hook(self, locale):
        page = SimpleNamespace(file=SimpleNamespace(locale=locale))
        return on_page_content("a cat, e.g. 5 kg", page, self.CONFIG, None)

    def test_polish_page_is_fixed(self):
        self.assertIn(NBSP, self.run_hook("pl"))

    def test_english_page_is_untouched(self):
        self.assertEqual(self.run_hook("en"), "a cat, e.g. 5 kg")

    def test_falls_back_to_site_language(self):
        page = SimpleNamespace(file=SimpleNamespace())
        self.assertIn(NBSP, on_page_content("a cat", page, self.CONFIG, None))


if __name__ == "__main__":
    unittest.main()
