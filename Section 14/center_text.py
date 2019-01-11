def center_text(*args):
    # text = ""
    # for arg in args:
    #     text += str(arg) + " "
    # text = "-".join(args)   # can't join ints to strings
    text = "-".join([str(arg) for arg in args])
    # text = "-".join(str(arg) for arg in args)   # no [] here makes it a generator expression
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


center_text("spam and eggs")
center_text(89)
center_text("woa, woa, hey, no")
center_text("hi", "hehe", 56)
