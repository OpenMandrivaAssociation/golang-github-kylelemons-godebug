# Run tests in check section
%bcond_without check

# https://github.com/kylelemons/godebug
%global goipath		github.com/kylelemons/godebug
%global forgeurl	https://github.com/kylelemons/godebug
Version:		1.1.0

%gometa

Summary:	Debugging helper utilities for Go
Name:		golang-github-kylelemons-godebug

Release:	1
Source0:	https://github.com/kylelemons/godebug/archive/v%{version}/godebug-%{version}.tar.gz
URL:		https://github.com/kylelemons/godebug
License:	ASL 2.0
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
BuildArch:	noarch

%description
Debugging helper utilities for Go.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n godebug-%{version}

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

