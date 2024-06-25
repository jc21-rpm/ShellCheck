%global debug_package %{nil}

Name:           ShellCheck
Version:        0.10.0
Release:        1%{?dist}
Summary:        Shell script analysis tool
License:        GPL-3.0-or-later
URL:            https://www.shellcheck.net/
Source:         https://github.com/koalaman/shellcheck/releases/download/v%{version}/shellcheck-v%{version}.linux.x86_64.tar.xz

%description
The goals of ShellCheck are:

* To point out and clarify typical beginner's syntax issues,
  that causes a shell to give cryptic error messages.
* To point out and clarify typical intermediate level semantic problems,
  that causes a shell to behave strangely and counter-intuitively.
* To point out subtle caveats, corner cases and pitfalls, that may cause an
  advanced user's otherwise working script to fail under future circumstances.

%prep
%setup -n shellcheck-v%{version}

%install
install -Dm0755 shellcheck %{buildroot}%{_bindir}/shellcheck

%files
%{_bindir}/shellcheck
%doc README.txt LICENSE.txt

%changelog
* Tue Jun 25 2024 Jamie Curnow <jc@jc21.com> - 0.10.0-1
- v0.10.0

* Wed Mar 22 2023 Jamie Curnow <jc@jc21.com> - 0.9.0-1
- v0.9.0
