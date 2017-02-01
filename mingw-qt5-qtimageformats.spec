%?mingw_package_header

%global qt_module qtimageformats
#%%global pre rc1

#%%global snapshot_date 20121112
#%%global snapshot_rev a0ec617b

%if 0%{?snapshot_date}
%global source_folder qt-%{qt_module}
%else
%global source_folder %{qt_module}-opensource-src-%{version}%{?pre:-%{pre}}
%endif

# first two digits of version
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-qt5-%{qt_module}
Version:        5.6.0
Release:        2%{?pre:.%{pre}}%{?snapshot_date:.git%{snapshot_date}.%{snapshot_rev}}%{?dist}
Summary:        Qt5 for Windows - QtImageFormats component

License:        GPLv3 with exceptions or LGPLv2 with exceptions
Group:          Development/Libraries
URL:            http://qt-project.org/

%if 0%{?snapshot_date}
# To regenerate:
# wget http://qt.gitorious.org/qt/%{qt_module}/archive-tarball/%{snapshot_rev} -O qt5-%{qt_module}-%{snapshot_rev}.tar.gz
Source0:        qt5-%{qt_module}-%{snapshot_rev}.tar.gz
%else
%if "%{?pre}" != ""
Source0:        http://download.qt-project.org/development_releases/qt/%{release_version}/%{version}-%{pre}/submodules/%{qt_module}-opensource-src-%{version}-%{pre}.tar.xz
%else
Source0:        http://download.qt-project.org/official_releases/qt/%{release_version}/%{version}/submodules/%{qt_module}-opensource-src-%{version}.tar.xz
%endif
%endif

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-qt5-qtbase >= 5.6.0
BuildRequires:  mingw32-libwebp
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw32-jasper

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-qt5-qtbase >= 5.6.0
BuildRequires:  mingw64-libwebp
BuildRequires:  mingw64-libtiff
BuildRequires:  mingw64-jasper


%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win32
%package -n mingw32-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtImageFormats component

%description -n mingw32-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win64
%package -n mingw64-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtImageFormats component

%description -n mingw64-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


%?mingw_debug_package


%prep
%setup -q -n %{source_folder}


%build
%mingw_qmake_qt5 ../%{qt_module}.pro
%mingw_make %{?_smp_mflags}


%install
%mingw_make install INSTALL_ROOT=$RPM_BUILD_ROOT


# Win32
%files -n mingw32-qt5-%{qt_module}
%doc LGPL_EXCEPTION.txt LICENSE.FDL LICENSE.GPLv2 LICENSE.LGPLv21 LICENSE.LGPLv3
%{mingw32_libdir}/qt5/plugins/imageformats/qdds.dll
%{mingw32_libdir}/qt5/plugins/imageformats/qicns.dll
%{mingw32_libdir}/qt5/plugins/imageformats/qjp2.dll
%{mingw32_libdir}/qt5/plugins/imageformats/qtga.dll
%{mingw32_libdir}/qt5/plugins/imageformats/qtiff.dll
%{mingw32_libdir}/qt5/plugins/imageformats/qwbmp.dll
%{mingw32_libdir}/qt5/plugins/imageformats/qwebp.dll
%{mingw32_libdir}/cmake/Qt5Gui/Qt5Gui_QDDSPlugin.cmake
%{mingw32_libdir}/cmake/Qt5Gui/Qt5Gui_QICNSPlugin.cmake
%{mingw32_libdir}/cmake/Qt5Gui/Qt5Gui_QJp2Plugin.cmake
%{mingw32_libdir}/cmake/Qt5Gui/Qt5Gui_QTgaPlugin.cmake
%{mingw32_libdir}/cmake/Qt5Gui/Qt5Gui_QTiffPlugin.cmake
%{mingw32_libdir}/cmake/Qt5Gui/Qt5Gui_QWbmpPlugin.cmake
%{mingw32_libdir}/cmake/Qt5Gui/Qt5Gui_QWebpPlugin.cmake

# Win64
%files -n mingw64-qt5-%{qt_module}
%doc LGPL_EXCEPTION.txt LICENSE.FDL LICENSE.GPLv2 LICENSE.LGPLv21 LICENSE.LGPLv3
%{mingw64_libdir}/qt5/plugins/imageformats/qdds.dll
%{mingw64_libdir}/qt5/plugins/imageformats/qicns.dll
%{mingw64_libdir}/qt5/plugins/imageformats/qjp2.dll
%{mingw64_libdir}/qt5/plugins/imageformats/qtga.dll
%{mingw64_libdir}/qt5/plugins/imageformats/qtiff.dll
%{mingw64_libdir}/qt5/plugins/imageformats/qwbmp.dll
%{mingw64_libdir}/qt5/plugins/imageformats/qwebp.dll
%{mingw64_libdir}/cmake/Qt5Gui/Qt5Gui_QDDSPlugin.cmake
%{mingw64_libdir}/cmake/Qt5Gui/Qt5Gui_QICNSPlugin.cmake
%{mingw64_libdir}/cmake/Qt5Gui/Qt5Gui_QJp2Plugin.cmake
%{mingw64_libdir}/cmake/Qt5Gui/Qt5Gui_QTgaPlugin.cmake
%{mingw64_libdir}/cmake/Qt5Gui/Qt5Gui_QTiffPlugin.cmake
%{mingw64_libdir}/cmake/Qt5Gui/Qt5Gui_QWbmpPlugin.cmake
%{mingw64_libdir}/cmake/Qt5Gui/Qt5Gui_QWebpPlugin.cmake


%changelog
* Wed Nov 23 2016 Michael Cronenworth <mike@cchtml.com> - 5.6.0-2
- Rebuilt for mingw-jasper update

* Sun Apr 10 2016 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.6.0-1
- Update to 5.6.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 30 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.5.1-1
- Update to 5.5.1

* Fri Aug  7 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.5.0-1
- Update to 5.5.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 22 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4.1-1
- Update to 5.4.1

* Thu Jan  1 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4.0-1
- Update to 5.4.0

* Sat Sep 20 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.3.2-1
- Update to 5.3.2

* Tue Jul  8 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.3.1-1
- Update to 5.3.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.3.0-1
- Update to 5.3.0

* Sat Feb  8 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.1-1
- Update to 5.2.1

* Sun Jan  5 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-1
- Update to 5.2.0

* Fri Nov 29 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-0.1.rc1
- Update to 5.2.0 RC1

* Sat Sep  7 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.1.1-1
- Update to 5.1.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 14 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.1.0-1
- Update to 5.1.0

* Sun Jun  2 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.2-2
- Added license files

* Fri May 10 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.2-1
- Update to 5.0.2

* Sat Feb  9 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1

* Fri Jan 11 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-1
- Update to Qt 5.0.0 Final

* Mon Nov 12 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-0.2.beta1.git20121112.a0ec617b
- Update to 20121112 snapshot (rev a0ec617b)
- Rebuild against latest mingw-qt5-qtbase
- Dropped pkg-config rename hack as it's unneeded now
- Dropped upstreamed patch

* Mon Sep 10 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-0.1.beta1
- Initial release

