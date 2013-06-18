%global packname  foreach
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}

Name:             R-%{packname}
Version:          1.3.2
Release:          2
Summary:          Foreach looping construct for R
Group:            Sciences/Mathematics
License:          Apache License (== 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-iterators R-codetools R-utils R-randomForest
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-iterators
BuildRequires:    R-codetools R-utils R-randomForest

%description
Support for the foreach looping construct.  Foreach is an idiom that
allows for iterating over elements in a collection, without the use of an
explicit loop counter.  This package in particular is intended to be used
for its return value, rather than for its side effects.  In that sense, it
is similar to the standard lapply function, but doesn't require the
evaluation of a function.  Using foreach without side effects also
facilitates executing the loop in parallel.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/unitTests
