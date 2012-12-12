# -*- python -*-

import waflib.Logs as msg

def pkg_deps(ctx):
    ctx.use_pkg('pkg-settings')
    return

def configure(ctx):
    return

def build(ctx):
    ctx(
        features="cxx cxxshlib",
        name="pkg-aa",
        source="src/pkg-aa.cxx",
        target="pkg-aa",
        includes=["inc"],
        export_includes=["inc"],
        use="ROOT",
        )
    def subst(s):
        import waflib.Utils
        return waflib.Utils.subst_vars(s, ctx.env)
    ctx.env['INCLUDES_pkg-aa'] = [subst('${INSTALL_AREA}/include')]
    ctx.env['LIBPATH_pkg-aa'] = [subst('${INSTALL_AREA}/lib')]
    ctx.env['LIB_pkg-aa'] = ['pkg-aa']
    
    incdir = ctx.path.find_node('inc')
    includes = incdir.ant_glob('**/*', dir=False)
    ctx.install_files(
        '${INSTALL_AREA}/include', includes, 
        relative_trick=True,
        cwd=incdir,
        )

    msg.info("ROOT-home: %s" % ctx.env.ROOT_HOME)
    return

def install(ctx):
    return
