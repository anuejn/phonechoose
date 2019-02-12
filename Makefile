default: build/with_prices.json

build/with_prices.json: build/linage_wiki.json
	python3 aggregate/get_ebay_prices.py $< > $@

build/linage_wiki.json: build/linage-wiki
	python3 aggregate/wiki2json.py $< > $@

build/linage-wiki:
	git clone --depth 1 https://github.com/LineageOS/lineage_wiki build/linage-wiki


.PHONY: clean
clean:
	rm -rf build
