#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : netcat
Version  : 0.7.1
Release  : 7
URL      : http://downloads.sourceforge.net/netcat/netcat-0.7.1.tar.gz
Source0  : http://downloads.sourceforge.net/netcat/netcat-0.7.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.1 GPL-2.0
Requires: netcat-bin
Requires: netcat-doc
Requires: netcat-locales
BuildRequires : bison

%description
Part of the GNU netcat project
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2, or (at your option)
any later version.

%package bin
Summary: bin components for the netcat package.
Group: Binaries

%description bin
bin components for the netcat package.


%package doc
Summary: doc components for the netcat package.
Group: Documentation

%description doc
doc components for the netcat package.


%package locales
Summary: locales components for the netcat package.
Group: Default

%description locales
locales components for the netcat package.


%prep
%setup -q -n netcat-0.7.1

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang netcat

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nc
/usr/bin/netcat

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*

%files locales -f netcat.lang 
%defattr(-,root,root,-)

