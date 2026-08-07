# DLMF-markdown

This repository is a minimalized version of the [NIST Digital Library of Mathematical Functions (DLMF)](https://dlmf.nist.gov/), containing just the math and the prose in markdown format. For the full version and a description of how it was made, see [`DLMF-mirror`](https://github.com/Novum-Mathematicum/DLMF-mirror).

The bibliography is available in `DLMF-mirror`. My recommendation is to go to `DLMF-mirror` and check the `bib` folder. For example, to find out what `Olver ([1997b](./bib/O.html#bib1809 "Asymptotics and Special Functions")` refers to exactly, simply open [`bib/bib1809.bib`](https://github.com/Novum-Mathematicum/DLMF-mirror/blob/main/html/bib/bib1809.bib), and there it is.

* `1` to `36`: The chapters. Each chapter is in a single folder. There is a file like `1.md` which is essentially a table of contents for the chapter, followed by `1.1.md` to `1.18.md` for the sections of the chapter.
* `toc.md`: all chapter names
* `toc_full.md`: all chapter and section names.
* `idx`: All indices.

## Intended use

I made this because I wanted to do classical mathematics and wrangle with those old classical mathematical functions, but I can't remember those obscure functions and their arcane properties. So I thought: "I can't remember these, and I can't figure out the right words to search on Google because Google doesn't take latex inputs. And Wolfram Alpha's AI is quite stupid and useless at fuzzy search... This is the perfect job for modern LLMs, if only they have access to those classical mathematical compendia!"

And thus I had the idea for getting a markdown version of the crown-jewel of human classical mathematics -- the DLMF! Markdown is the best format for LLM ingest, way better than `html`. Sure, I think in a few years, this will be obsoleted, but I think this is still a better use of my time than studying all these things myself, on the off chance that I in the next 5 years would have a use for one of the hundreds of equations in those big books.

This repository is currently intended for use by LLM-human cyborgs, though you are encouraged to use it however you see fit, of course. The suggested use is as follows:

* If you are an LLM working online in RESTful style, then ingest this repo via a GitHub API call, such as gitingest.
* Otherwise, download [`DLMF-mirror`](https://github.com/Novum-Mathematicum/DLMF-mirror). It contains both the plain markdown files fit for LLM textual ingest, and the rich html files fit for human visuokinesthetic ingest.

## Notes

DLMF uses a few minor variants of standard LaTeX, which I have preserved without change:

* `\,` works as an invisible multiplication symbol. It seems to have no effect on the visual presentation of the formulas, and thus is purely semantic.
* `\frac{a}{b}` means a fraction `\frac{a}{b}`, but looks like `a / b`. It means "inline fraction".
* `a` means "new variable `a`". It is used exclusively within infoboxes to denote that a symbol has no secret meaning. For example, `z` means, "The symbol `z` really has no special meaning. It does not mean something cool like Riemann's Zeta function. No. It literally is just a variable.". I'm pretty sure `NVar` means "new variable" or maybe "nothing-special variable".
* `\cfracstyle` I don't know what this is supposed to mean, but it only appeared once while talking about the presentation of continued fractions, in Section `1.12`.
