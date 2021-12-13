#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-spatstat.linnet
Version  : 2.3.1
Release  : 5
URL      : https://cran.r-project.org/src/contrib/spatstat.linnet_2.3-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/spatstat.linnet_2.3-1.tar.gz
Summary  : Linear Networks Functionality of the 'spatstat' Family
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-spatstat.linnet-lib = %{version}-%{release}
Requires: R-spatstat.core
Requires: R-spatstat.data
Requires: R-spatstat.geom
Requires: R-spatstat.sparse
Requires: R-spatstat.utils
BuildRequires : R-spatstat.core
BuildRequires : R-spatstat.data
BuildRequires : R-spatstat.geom
BuildRequires : R-spatstat.sparse
BuildRequires : R-spatstat.utils
BuildRequires : buildreq-R

%description
and provides functionality for geometrical operations,
	     data analysis and modelling of data on a linear network,
	     in the 'spatstat' family of packages.
	     Contains definitions and support for linear networks, including creation of networks, geometrical measurements, topological connectivity, geometrical operations such as inserting and deleting vertices, intersecting a network with another object, and interactive editing of networks.
	     Data types defined on a network include point patterns, pixel images, functions, and tessellations.
	     Exploratory methods include kernel estimation of intensity on a network, K-functions and pair correlation functions on a network, simulation envelopes, nearest neighbour distance and empty space distance, relative risk estimation with cross-validated bandwidth selection. Formal hypothesis tests of random pattern (chi-squared, Kolmogorov-Smirnov, Monte Carlo, Diggle-Cressie-Loosmore-Ford, Dao-Genton, two-stage Monte Carlo) and tests for covariate effects (Cox-Berman-Waller-Lawson, Kolmogorov-Smirnov, ANOVA) are also supported.
	Parametric models can be fitted to point pattern data using the function lppm() similar to glm(). Only Poisson models are implemented so far. Models may involve dependence on covariates and dependence on marks. Models are fitted by maximum likelihood.
	Fitted point process models can be simulated, automatically. Formal hypothesis tests of a fitted model are supported (likelihood ratio test, analysis of deviance, Monte Carlo tests) along with basic tools for model selection (stepwise(), AIC()) and variable selection (sdr). Tools for validating the fitted model include simulation envelopes, residuals, residual plots and Q-Q plots, leverage and influence diagnostics, partial residuals, and added variable plots.
	Random point patterns on a network can be generated using a variety of models.

%package lib
Summary: lib components for the R-spatstat.linnet package.
Group: Libraries

%description lib
lib components for the R-spatstat.linnet package.


%prep
%setup -q -c -n spatstat.linnet
cd %{_builddir}/spatstat.linnet

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639424719

%install
export SOURCE_DATE_EPOCH=1639424719
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spatstat.linnet
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spatstat.linnet
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spatstat.linnet
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc spatstat.linnet || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/spatstat.linnet/CITATION
/usr/lib64/R/library/spatstat.linnet/DESCRIPTION
/usr/lib64/R/library/spatstat.linnet/INDEX
/usr/lib64/R/library/spatstat.linnet/Meta/Rd.rds
/usr/lib64/R/library/spatstat.linnet/Meta/features.rds
/usr/lib64/R/library/spatstat.linnet/Meta/hsearch.rds
/usr/lib64/R/library/spatstat.linnet/Meta/links.rds
/usr/lib64/R/library/spatstat.linnet/Meta/nsInfo.rds
/usr/lib64/R/library/spatstat.linnet/Meta/package.rds
/usr/lib64/R/library/spatstat.linnet/NAMESPACE
/usr/lib64/R/library/spatstat.linnet/NEWS
/usr/lib64/R/library/spatstat.linnet/R/spatstat.linnet
/usr/lib64/R/library/spatstat.linnet/R/spatstat.linnet.rdb
/usr/lib64/R/library/spatstat.linnet/R/spatstat.linnet.rdx
/usr/lib64/R/library/spatstat.linnet/doc/packagesizes.txt
/usr/lib64/R/library/spatstat.linnet/help/AnIndex
/usr/lib64/R/library/spatstat.linnet/help/aliases.rds
/usr/lib64/R/library/spatstat.linnet/help/macros/defns.Rd
/usr/lib64/R/library/spatstat.linnet/help/paths.rds
/usr/lib64/R/library/spatstat.linnet/help/spatstat.linnet.rdb
/usr/lib64/R/library/spatstat.linnet/help/spatstat.linnet.rdx
/usr/lib64/R/library/spatstat.linnet/html/00Index.html
/usr/lib64/R/library/spatstat.linnet/html/R.css
/usr/lib64/R/library/spatstat.linnet/ratfor/Makefile
/usr/lib64/R/library/spatstat.linnet/ratfor/dppll.r
/usr/lib64/R/library/spatstat.linnet/ratfor/inxypOld.r
/usr/lib64/R/library/spatstat.linnet/tests/testsAtoK.R
/usr/lib64/R/library/spatstat.linnet/tests/testsL.R
/usr/lib64/R/library/spatstat.linnet/tests/testsMtoZ.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/spatstat.linnet/libs/spatstat.linnet.so
/usr/lib64/R/library/spatstat.linnet/libs/spatstat.linnet.so.avx2
/usr/lib64/R/library/spatstat.linnet/libs/spatstat.linnet.so.avx512
