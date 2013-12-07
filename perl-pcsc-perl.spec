%define modname pcsc-perl
%define version 1.4.11

Summary:	Perl interface to the PC/SC smart card library
Name:		perl-%{modname}
Version:	%{version}
Release:	4
License:	GPLv2
Group:		Development/Perl
Url:		http://ludovic.rousseau.free.fr/softwares/pcsc-perl/
Source0:	http://ludovic.rousseau.free.fr/softwares/pcsc-perl/%{modname}-%{version}.tar.bz2
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	pkgconfig(libpcsclite)

%description
This package contains a Perl wrapper to the PC/SC smartcard library
(pcsc-lite) from MUSCLE together with some small examples.

%prep
%setup -qn %{modname}-%{version}
find -name \*.pm | xargs chmod 644

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# this needs a smart card reader configured and with a
# card inserted
#%%make test

%install
%makeinstall_std

%files
%doc LICENCE README* examples Changelog
%{perl_vendorlib}/*/Chipcard
%{perl_vendorlib}/*/auto/Chipcard
%{_mandir}/man3/*

