#!/bin/bash

function downimg() {
  out=out.${1##*.}
  curl $1 > $out
  convert $out out.png
  pngquant out.png
  mv out-fs8.png $2
}
