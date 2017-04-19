This is an attempt to list of **Github** repositories that have **build-less** gh-pages demos/samples/examples, for the
JavaScript following MVC/MVVM frameworks:

* 152 [AngularJS](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#AngularJS)
* 83 [Vue](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Vue)
* 81 [Ember](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Ember)
* 59 [Backbone](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Backbone)
* 58 [Ractive](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Ractive)
* 53 [React](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#React)
* 41 [Knockout](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Knockout)
* 37 [Mithril](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Mithril)
* 32 [Riot](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Riot)
* 27 [Enyo](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Enyo)
* 17 [Angular](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Angular)
* 14 [Polymer](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Polymer)
* 12 [Flight](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Flight)
* 12 [Cycle](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Cycle)
* 11 [Marko](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Marko)
* 10 [Aurelia](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Aurelia)
* 9 [Inferno](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/#Inferno)
* 0 Svelte

Buildless examples serve as good tools for learning (and comparing) such frameworks.  Some people (like me) greatly
prefer self-contained/clonable/runnable examples to tutorials and reference docs.

JsFiddle, Codepen, Plunker [and alike](https://www.quora.com/What-are-some-alternatives-to-http-jsfiddle-net) are similar places to discover buildless examples.  So is StackOverflow, but the example code
inlined isn't runnable, so is imperfect (unless there's a link to

This page doesn't show true popularity of these frameworks - Newer technologies like Angular (successor to AngularJS) greatly
rely on a build to use it, whereas the first few years of AngularJS didn't.

## To update the data:

```
# Install sponge, and ImageMagick for your platform
pip3 install selenium
cd docs
rm *.json
rm -rf results/
python3 search_gh_for_frameworks.py your-github-id # and your password when prompted
sort search_results.json | sponge search_results.json
rm *-gh-pages.txt
python3 subset-to-framework-using-ghpages.py # kiss goodbye to 12 hours or so
# Make thumbnails using ImageMagick
for f in `find . -name "*.png" | sed '/\.thumb\./d'`; do convert $f -resize 10% ${f/.png/.thumb.png}; done
# delete non-thumbnails
for f in `find . -name "*.png" | sed '/\.thumb\./d'`; do rm ${f}; done
git add .
git commit -m "more"
```

You should probably run the thing in VM as Chrome could have a zeroday vuln, that one of these could take advantage of.

For AngularJS and Angular - there is an attempt to

Site: [javascript-frameworks-with-ghpages-demos](https://paul-hammant.github.io/javascript-frameworks-with-ghpages-demos/)

Notes:

1. It is doubtless
incomplete especially as Github [don't have gh-pages branches anymore](https://github.com/blog/2228-simpler-github-pages-publishing).

2. There's no fine grained breakdown of versions

3. The order is alphabetical, with number of 'stars' (descending) within that

4. I wish framework maintainers curate this list themselves, as "you should use my framework, look at these community demos" is a powerful selling technique.

