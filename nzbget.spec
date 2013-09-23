%define beta %{nil}
%define scmrev %{nil}

Name: nzbget
Version: 11.0
%if "%{beta}" == ""
%if "%{scmrev}" == ""
Release: 1
Source: http://sourceforge.net/projects/nzbget/files/nzbget-%{version}.tar.gz
%else
Release: 0.%{scmrev}.1
Source: %{name}-%{scmrev}.tar.xz
%endif
%else
%if "%{scmrev}" == ""
Release: 0.%{beta}.1
Source: %{name}-%{version}%{beta}.tar.bz2
%else
Release: 0.%{beta}.0.%{scmrev}.1
Source: %{name}-%{scmrev}.tar.xz
%endif
%endif
Summary: NZB file downloader
URL: http://nzbget.sf.net/
License: GPL
Group: Networking/File transfer
BuildRequires: %{_lib}par2-devel
BuildRequires: pkgconfig(sigc++-2.0)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(ncursesw)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(zlib)

%description
NZBGet is a cross-platform binary newsgrabber for nzb files, written in C++. 
It supports client/server mode, automatic par-check/-repair and
web-interface.

NZBGet requires low system resources and runs great on routers, NAS-devices
and media players. 

%prep
%if "%{scmrev}" == ""
%setup -q -n %{name}-%{version}%{beta}
%else
%setup -q -n %{name}
%endif
%configure

%build
%make

%install
%makeinstall_std

%files
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/%{name}
%doc %{_docdir}/%{name}
