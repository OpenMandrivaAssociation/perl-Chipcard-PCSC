%define modname Chipcard-PCSC

Summary:	Perl interface to the PC/SC smart card library
Name:		perl-%{modname}
Version:	1.4.16
Release:	3
License:	GPLv2
Group:		Development/Perl
Url:		https://pcsc-perl.apdu.fr/
Source0:	https://pcsc-perl.apdu.fr/%{modname}-v%{version}.tar.gz
BuildRequires:	make
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	pkgconfig(libpcsclite)
%rename perl-pcsc-perl

%description
This package contains a Perl wrapper to the PC/SC smartcard library
(pcsc-lite) from MUSCLE together with some small examples.

%prep
%autosetup -n %{modname}-v%{version} -p1
find -name \*.pm | xargs chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%install
%make_install

%files
%doc LICENCE README* Changelog
%{perl_vendorarch}/Chipcard
%{perl_vendorarch}/auto/Chipcard
%{_mandir}/man3/*
