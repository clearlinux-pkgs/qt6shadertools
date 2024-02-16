#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: da8b975
#
Name     : qt6shadertools
Version  : 6.6.2
Release  : 9
URL      : https://download.qt.io/official_releases/qt/6.6/6.6.2/submodules/qtshadertools-everywhere-src-6.6.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/6.6/6.6.2/submodules/qtshadertools-everywhere-src-6.6.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0 MIT
Requires: qt6shadertools-lib = %{version}-%{release}
Requires: qt6shadertools-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : mesa-dev
BuildRequires : qt6base-dev
BuildRequires : qtbase-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# News
1. Visual Studio 2013 is no longer supported
Microsoft Visual Studio 2013 is no longer officially supported. \
Please upgrade to at least Visual Studio 2015.

%package dev
Summary: dev components for the qt6shadertools package.
Group: Development
Requires: qt6shadertools-lib = %{version}-%{release}
Provides: qt6shadertools-devel = %{version}-%{release}
Requires: qt6shadertools = %{version}-%{release}

%description dev
dev components for the qt6shadertools package.


%package lib
Summary: lib components for the qt6shadertools package.
Group: Libraries
Requires: qt6shadertools-license = %{version}-%{release}

%description lib
lib components for the qt6shadertools package.


%package license
Summary: license components for the qt6shadertools package.
Group: Default

%description license
license components for the qt6shadertools package.


%prep
%setup -q -n qtshadertools-everywhere-src-6.6.2
cd %{_builddir}/qtshadertools-everywhere-src-6.6.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1708119113
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1708119113
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6shadertools
cp %{_builddir}/qtshadertools-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6shadertools/b073f11f0c81a95ab5e32aa6b5d23a5955a95274 || :
cp %{_builddir}/qtshadertools-everywhere-src-%{version}/LICENSES/GFDL-1.3-no-invariants-only.txt %{buildroot}/usr/share/package-licenses/qt6shadertools/715f995f11805ee85601834220c43b082f457ea3 || :
cp %{_builddir}/qtshadertools-everywhere-src-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/qt6shadertools/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/qtshadertools-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6shadertools/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/qtshadertools-everywhere-src-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6shadertools/f45ee1c765646813b442ca58de72e20a64a7ddba || :
cp %{_builddir}/qtshadertools-everywhere-src-%{version}/src/3rdparty/SPIRV-Cross/KHRONOS-LICENSE.txt %{buildroot}/usr/share/package-licenses/qt6shadertools/6a78febdc9421a96e46b0a2a9890563124c6d71f || :
cp %{_builddir}/qtshadertools-everywhere-src-%{version}/src/3rdparty/SPIRV-Cross/LICENSE %{buildroot}/usr/share/package-licenses/qt6shadertools/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/qtshadertools-everywhere-src-%{version}/src/3rdparty/glslang/LICENSE.txt %{buildroot}/usr/share/package-licenses/qt6shadertools/f77668fa8c7bb3dc2788af730150c401bd723fed || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/qt6/bin/qsb
/usr/lib64/qt6/bin/qsb
/usr/lib64/qt6/metatypes/qt6shadertools_relwithdebinfo_metatypes.json
/usr/lib64/qt6/mkspecs/modules/qt_lib_shadertools.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_shadertools_private.pri
/usr/lib64/qt6/modules/ShaderTools.json

%files dev
%defattr(-,root,root,-)
/usr/include/QtShaderTools/6.6.2/QtShaderTools/private/qshaderrewriter_p.h
/usr/include/QtShaderTools/6.6.2/QtShaderTools/private/qspirvcompiler_p.h
/usr/include/QtShaderTools/6.6.2/QtShaderTools/private/qspirvshader_p.h
/usr/include/QtShaderTools/6.6.2/QtShaderTools/private/qspirvshaderremap_p.h
/usr/include/QtShaderTools/6.6.2/QtShaderTools/private/qtshadertoolsexports_p.h
/usr/include/QtShaderTools/6.6.2/QtShaderTools/private/qtshadertoolsglobal_p.h
/usr/include/QtShaderTools/6.6.2/QtShaderTools/rhi/qshaderbaker.h
/usr/include/QtShaderTools/QtShaderTools
/usr/include/QtShaderTools/QtShaderToolsDepends
/usr/include/QtShaderTools/QtShaderToolsVersion
/usr/include/QtShaderTools/qtshadertoolsexports.h
/usr/include/QtShaderTools/qtshadertoolsglobal.h
/usr/include/QtShaderTools/qtshadertoolsversion.h
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/QtShaderToolsTestsConfig.cmake
/usr/lib64/cmake/Qt6ShaderTools/Qt6ShaderToolsAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6ShaderTools/Qt6ShaderToolsConfig.cmake
/usr/lib64/cmake/Qt6ShaderTools/Qt6ShaderToolsConfigVersion.cmake
/usr/lib64/cmake/Qt6ShaderTools/Qt6ShaderToolsConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6ShaderTools/Qt6ShaderToolsDependencies.cmake
/usr/lib64/cmake/Qt6ShaderTools/Qt6ShaderToolsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6ShaderTools/Qt6ShaderToolsTargets.cmake
/usr/lib64/cmake/Qt6ShaderTools/Qt6ShaderToolsVersionlessTargets.cmake
/usr/lib64/cmake/Qt6ShaderToolsTools/Qt6ShaderToolsMacros.cmake
/usr/lib64/cmake/Qt6ShaderToolsTools/Qt6ShaderToolsToolsAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6ShaderToolsTools/Qt6ShaderToolsToolsConfig.cmake
/usr/lib64/cmake/Qt6ShaderToolsTools/Qt6ShaderToolsToolsConfigVersion.cmake
/usr/lib64/cmake/Qt6ShaderToolsTools/Qt6ShaderToolsToolsConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6ShaderToolsTools/Qt6ShaderToolsToolsDependencies.cmake
/usr/lib64/cmake/Qt6ShaderToolsTools/Qt6ShaderToolsToolsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6ShaderToolsTools/Qt6ShaderToolsToolsTargets.cmake
/usr/lib64/cmake/Qt6ShaderToolsTools/Qt6ShaderToolsToolsVersionlessTargets.cmake
/usr/lib64/libQt6ShaderTools.prl
/usr/lib64/libQt6ShaderTools.so
/usr/lib64/pkgconfig/Qt6ShaderTools.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libQt6ShaderTools.so.6.6.2
/usr/lib64/libQt6ShaderTools.so.6
/usr/lib64/libQt6ShaderTools.so.6.6.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6shadertools/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/qt6shadertools/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qt6shadertools/6a78febdc9421a96e46b0a2a9890563124c6d71f
/usr/share/package-licenses/qt6shadertools/715f995f11805ee85601834220c43b082f457ea3
/usr/share/package-licenses/qt6shadertools/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qt6shadertools/b073f11f0c81a95ab5e32aa6b5d23a5955a95274
/usr/share/package-licenses/qt6shadertools/f45ee1c765646813b442ca58de72e20a64a7ddba
/usr/share/package-licenses/qt6shadertools/f77668fa8c7bb3dc2788af730150c401bd723fed
