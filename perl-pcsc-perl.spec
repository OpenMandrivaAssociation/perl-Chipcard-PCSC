%define modname pcsc-perl
%define version 1.4.14
%define _disable_lto 1

Summary:	Perl interface to the PC/SC smart card library
Name:		perl-%{modname}
Version:	%perl_convert_version 1.4.14
Release:	4
License:	GPLv2
Group:		Development/Perl
Url:		http://ludovic.rousseau.free.fr/softwares/pcsc-perl/
Source0:	http://ludovic.rousseau.free.fr/softwares/pcsc-perl/pcsc-perl-%{version}.tar.bz2
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	pkgconfig(libpcsclite)

%description
This package contains a Perl wrapper to the PC/SC smartcard library
(pcsc-lite) from MUSCLE together with some small examples.

%prep
%autosetup -n %{modname}-%{version} -p1
find -name \*.pm | xargs chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
# this needs a smart card reader configured and with a
# card inserted
#make test

%install
%make_install

%files
%doc LICENCE README* examples Changelog
%{perl_vendorarch}/Chipcard
%{perl_vendorarch}/auto/Chipcard
%{_mandir}/man3/*
