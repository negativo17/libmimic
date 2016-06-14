Name:           libmimic
Version:        1.0.4
Release:        9%{?dist}
Summary:        Encoding/decoding library for Mimic V2.x
License:        LGPLv2+
URL:            http://farsight.sourceforge.net/

Source0:        http://downloads.sourceforge.net/farsight/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
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
%setup -q

%build
autoreconf -vif
%configure --disable-static
make %{?_smp_mflags} libmimic_la_LIBADD="-lglib-2.0 -lm"

%install
%make_install
find %{buildroot} -name "*.la" -delete

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

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
* Tue Jun 14 2016 Simone Caronni <negativo17@gmail.com> - 1.0.4-9
- Clean up SPEC file.

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 02 2014 Hans de Goede <j.w.r.degoede@gmail.com> - 1.0.4-7
- Stop using pre-built docs (rf3114)

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.0.4-6
- Mass rebuilt for Fedora 19 Features

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov  7 2009 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.4-4
- Fix multilib conflict in -devel package (rf858)

* Fri Aug  7 2009 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.4-3
- Actually link to glib-2.0 not the ancient glib (issue
  caused by the undefined-non-weak-symbol fix) (rf487)

* Thu Aug  6 2009 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.4-2
- Fix undefined-non-weak-symbol in libmimic.so.0 (rf487)

* Sun Mar 29 2009 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.4-1
- First version of the RPM Fusion package
