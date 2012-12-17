# -*- python -*-

import waflib.Logs as msg

def pkg_deps(ctx):
    ctx.use_pkg('pkg-settings')
    return

def configure(ctx):
    return

def build(ctx):
    ctx.build_linklib(
        name="pkg-aa",
        source="src/pkg-aa.cxx",
        use="ROOT",
        )
    
    ctx(
        features     = 'py',
        name         = 'py-pkgaa',
        source       = 'python/pkgaa.py',
        install_path = '${INSTALL_AREA}/python',
        )

    msg.info("ROOT-home: %s" % ctx.env.ROOT_HOME)
    return

def install(ctx):
    return
