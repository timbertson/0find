VERSION=0.1
NAME=0find
FILES=0find 0find.py
BUILD=0inst

package:
	mkdir -p $(BUILD)
	tar czf $(BUILD)/$(NAME)-$(VERSION).tgz $(FILES)
	0publish-gfxmonk $(NAME) $(VERSION)

upload:
	(cd ~/Sites/gfxmonk && make upload)

0: package upload
