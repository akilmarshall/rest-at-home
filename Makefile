# Makefile to convert all .dot files in the current directory to .png in img/

DOTFILES := $(wildcard *.gv)
PNGS := $(patsubst %.gv,img/%.png,$(DOTFILES))

all: $(PNGS)

img/%.png: %.gv img
	dot -Tpng $< -o $@

show-%: %.gv
	dot -Txlib $<

img:
	mkdir -p img

clean:
	rm -f img/*.png
	rm *.png
