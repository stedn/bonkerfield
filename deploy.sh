#!/bin/bash
bundle exec jekyll build
git checkout gh-pages
cp -r _site/* .
git add -u
git add *
git commit -m 'ci'
git push origin gh-pages
git checkout master
