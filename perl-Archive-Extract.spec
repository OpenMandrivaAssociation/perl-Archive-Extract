%define	modname	Archive-Extract
%define modver 0.88

Summary:	A generic archive extracting mechanism
Name:		perl-%{modname}
Version:	%{modver}
Release:	1
License:	Artistic/GPLv2
Group:		Development/Perl
Url:		https://github.com/jib/archive-extract
Source0:	https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Archive-Extract-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test::More)
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
