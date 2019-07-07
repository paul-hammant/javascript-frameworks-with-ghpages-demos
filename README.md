# What is in the repo?

This is an attempt to list of **Github** repositories that have **build-less** Github-Pages demos/samples/examples. At least for the
JavaScript following MVC/MVVM frameworks:

* [AngularJS](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#AngularJS) - 152 examples
* [Vue](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Vue) - 83 examples
* [Ember](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Ember) - 81 examples
* [Backbone](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Backbone) - 59 examples
* [Ractive](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Ractive) - 58 examples
* [React](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#React) - 53 examples
* [Knockout](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Knockout) - 41 examples
* [Mithril](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Mithril) - 37 examples
* [Riot](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Riot) -32 examples
* [Enyo](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Enyo) -27 examples
* [Angular](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Angular) -17 examples
* [Polymer](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Polymer) - 14 examples
* [Flight](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Flight) - 12 examples
* [Cycle](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Cycle) - 12 examples
* [Marko](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Marko)- 11 examples
* [Aurelia](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Aurelia) - 10 examples
* [Inferno](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Inferno) - 9 examples
* Svelte - no examples yet

Buildless examples serve as good tools for learning (and comparing) such frameworks.  Some people (like me) greatly
prefer self-contained/clonable/runnable examples to tutorials and reference docs.

JsFiddle, Codepen, Plunker [and alike](https://www.quora.com/What-are-some-alternatives-to-http-jsfiddle-net) are similar places to discover buildless examples.  So is StackOverflow, but the example code
inlined isn't runnable, so is imperfect (unless there's a link to

This page doesn't show true popularity of these frameworks - Newer technologies like Angular (successor to AngularJS) greatly
rely on a build to use them, whereas the first few years of AngularJS (2009-11) didn't. Some technologies like Meteor cannot possibly
be build-less, and therefore are not listed at all.

# WTF is buildless?

No NPM, WebPack, Gulp, Babel, Grunt etc.  Just use the JavaSript tech directly in a HTML page pretty much "as is". From 1995 to 2005 this was he only way to do it.

# To update the data:

## Install sponge, ChromeDriver and ImageMagick for your platform

```
brew install moreutils imagemagick
brew cask install chromedriver
```

## Get the list of analyzable repos

```
pip3 install selenium
cd docs
rm *.json
rm -rf results/
python3 search_gh_for_frameworks.py your-github-id # and your password when prompted
sort search_results.json | sponge search_results.json
```

## Using Selenium load up each Github-Pages repo

```
rm *-gh-pages.txt
python3 subset-to-framework-using-ghpages.py # kiss goodbye to 12 hours or so
```

## Make thumbnails using ImageMagick

```
for f in `find . -name "*.png" | sed '/\.thumb\./d'`; do convert $f -resize 10% ${f/.png/.thumb.png}; done
```

## delete non-thumbnails

```
for f in `find . -name "*.png" | sed '/\.thumb\./d'`; do rm ${f}; done
git add .
git commit -m "more"
```

You should probably run these scripts in disposable VM as Chrome could have a zero-day vuln allowing a hacker to install software on your machine.

For AngularJS and Angular - there is an attempt to detect the framework in the browser by looking for a known property `window.angular.version.full`.

# Contributions

Pull-requests welcome. Especially for the false positives/negatives and the framework version detection logic (in Selenium, once loaded).

# Notes

1. The mechanism of looking for gh-pages is brute force - it just speculatively looks for `index.html` on the `ORG_OR_USER.github.io/REPO` site (with Selenium)

2. There's no fine grained breakdown of versions, other than for Angular/JS

3. The order within each framework is by 'stars' (descending)

4. I wish framework maintainers would curate these lists themselves, as "you should use my framework, look at these community demos" is a powerful selling technique.

