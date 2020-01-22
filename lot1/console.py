#!/usr/bin/env python3

from cleo import Application
from skeleton import SkeletonCommand


app = Application()
app.add(SkeletonCommand())

if __name__ == '__main__':
	app.run()
