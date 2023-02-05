# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}

Summary: uuid library from util-linux
Name: uuid
Version: 1.3.0
Release: 2%{?dist}
License: GPLv3+
URL: https://github.com/danielhams/dicl
Source: https://mirrors.edge.kernel.org/pub/linux/utils/util-linux/v2.34/util-linux-2.34.tar.gz

Patch100: libuuid.sgifixes.patch

BuildRequires: gcc
BuildRequires: automake, autoconf, libtool

%description
uuid library from the util-linux package.

%package devel
Summary: Header files and libraries for the uuid library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
uuid-devel contains the header files and libraries needed
to develop programs that use uuid library.

%prep
%setup -q -n util-linux-2.34
%patch100 -p1 -b .sgifixes

%build
%{configure} --disable-all-programs --enable-libuuid
make %{?_smp_mflags} libuuid.la

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} INSTALL='install -p'
# Remove stuff we won't use
rm -rf $RPM_BUILD_ROOT%{_libdir}/libuuid.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale

%files
%{_libdir}/libuuid.so.*

%files devel
%{_libdir}/libuuid.a
%{_libdir}/libuuid.so
%{_libdir}/pkgconfig/uuid.pc
%{_includedir}/uuid
%{_mandir}/man3

%changelog
* Sat Apr 25 2020 Daniel Hams <daniel.hams@gmail.com> - 1.3.0-2
- Avoid gettext use to avoid pulling in gettext/libintl etc.

* Fri Nov 29 2019 Daniel Hams <daniel.hams@gmail.com> - 1.3.0-1
- First build
