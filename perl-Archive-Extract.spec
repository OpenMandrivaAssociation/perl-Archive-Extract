%define	modname	Archive-Extract
%define modver 0.72

Summary:	A generic archive extracting mechanism
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	Artistic/GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Archive/Archive-Extract-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(IPC::Cmd) >= 0.360.0
BuildRequires:	perl(Module::Load::Conditional) >= 0.40.0
BuildRequires:	perl-version
BuildRequires:	perl-JSON-PP

%description
Archive::Extract is a generic archive extraction mechanism.

It allows you to extract any archive file of the type .tar, .tar.gz, .gz, .Z,
tar.bz2, .tbz, .bz2 or .zip without having to worry how it does so, or use
different interfaces for each type by using either perl modules, or commandline
tools on your system.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README CHANGES
%{perl_vendorlib}/Archive/*
%{_mandir}/man3/*



