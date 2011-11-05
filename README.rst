fpsync
======
fpsync is a tool for synchronising files over multiple systems, using rsync.
Unlike unison, it preserves hard links.

Setting up fpsync
-----------------
1. Place ``fpsync``, ``dircopy`` and ``highlight_newer.py`` on your path.
2. Customize ``fpsyncrc-example.py`` and ``fpsyncrc-example.excludes``.
3. Run ``fpsync --dry-run --config fpsyncrc-example.py DIR`` (with DIR either
   "up" or "down") to make sure it does what you want

