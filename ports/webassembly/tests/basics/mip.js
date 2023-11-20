/*
Tests to write once tests are running successfully:
mip.install("pkgname")  # Installs the latest version of "pkgname" (and dependencies)
mip.install("pkgname", version="x.y")  # Installs version x.y of "pkgname"
mip.install("pkgname", mpy=False)  # Installs the source version (i.e. .py rather than .mpy files)
mip.install("pkgname", target="third-party")
sys.path.append("third-party")
mip.install("http://example.com/x/y/foo.py")
mip.install("http://example.com/x/y/foo.mpy")
mip.install("github:org/repo/path/foo.py")  # Uses default branch
mip.install("github:org/repo/path/foo.py", version="branch-or-tag")  # Optionally specify the branch or tag
mip.install("http://example.com/x/package.json")
mip.install("github:org/user/path/package.json")
mip.install("http://example.com/x/")
mip.install("github:org/repo")  # Uses default branch of that repo
mip.install("github:org/repo", version="branch-or-tag")
*/