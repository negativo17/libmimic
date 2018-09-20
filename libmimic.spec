Name:           libmimic
Version:        1.0.4
Release:        11%{?dist}
Summary:        Encoding/decoding library for Mimic V2.x
License:        LGPLv2+
URL:            https://www.freedesktop.org/wiki/Software/Farstream/

Source0:        http://downloads.sourceforge.net/farsight/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  libtool

%description
libmimic is an open source video encoding/decoding library for Mimic V2.x-
encoded content (fourCC: ML20), which is the encoding used by MSN Messenger
for webcam conversations.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
libmimic is an open source video encoding/decoding library for Mimic V2.x-
encoded content (fourCC: ML20), which is the encoding used by MSN Messenger
for webcam conversations.

The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup

%build
autoreconf -vif
%configure --disable-static
make %{?_smp_mflags} libmimic_la_LIBADD="-lglib-2.0 -lm"

%install
%make_install
find %{buildroot} -name "*.la" -delete

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS README
%{_libdir}/*.so.*

%files devel
%doc doc/api/html
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Sep 20 2018 Simone Caronni <negativo17@gmail.com> - 1.0.4-11
- Add GCC build requirement.

* Fri Jun 29 2018 Simone Caronni <negativo17@gmail.com> - 1.0.4-10
- Update SPEC file.

* Tue Jun 14 2016 Simone Caronni <negativo17@gmail.com> - 1.0.4-9
- Clean up SPEC file.

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
