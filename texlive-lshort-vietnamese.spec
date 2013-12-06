# revision 15878
# category Package
# catalog-ctan /info/lshort/vietnamese
# catalog-date 2007-03-09 12:50:50 +0100
# catalog-license lppl
# catalog-version 4.00
Name:		texlive-lshort-vietnamese
Version:	4.00
Release:	6
Summary:	vietnamese version of the LaTeX introduction
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/vietnamese
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-vietnamese.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-vietnamese.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
Vietnamese version of A Short Introduction to LaTeX2e.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-vietnamese/README
%doc %{_texmfdistdir}/doc/latex/lshort-vietnamese/lshort-vi.pdf
%doc %{_texmfdistdir}/doc/latex/lshort-vietnamese/src/LocalVariables
%doc %{_texmfdistdir}/doc/latex/lshort-vietnamese/src/Makefile
%doc %{_texmfdistdir}/doc/latex/lshort-vietnamese/src/README.txt
%doc %{_texmfdistdir}/doc/latex/lshort-vietnamese/src/abbr.tex
%doc %{_texmfdistdir}/doc/latex/lshort-vietnamese/src/biblio.tex
%doc %{_texmfdistdir}/doc/latex/lshort-vietnamese/src/contrib.tex
%doc %{_texmfdistdir}/doc/latex/lshort-vietnamese/src/custom.tex
%doc %{_texmfdistdir}/doc/latex/lshort-vietnamese/src/fancyhea.sty
%doc %{_texmfdistdir}/doc/latex/lshort-vietnamese/src/graphic.tex
%doc %{_texmfdistdir}/doc/latex/lshort-vietnamese/src/lshort-print-vi.tex
%doc %{_texmfdistdir}/doc/latex/lshort-vietnamese/src/lshort-vi.sty
%doc %{_texmfdistdir}/doc/latex/lshort-vietnamese/src/lshort-vi.tex
%doc %{_texmfdistdir}/doc/latex/lshort-vietnamese/src/lssym.tex
%doc %{_texmfdistdir}/doc/latex/lshort-vietnamese/src/math.tex
%doc %{_texmfdistdir}/doc/latex/lshort-vietnamese/src/mylayout.sty
%doc %{_texmfdistdir}/doc/latex/lshort-vietnamese/src/overview.tex
%doc %{_texmfdistdir}/doc/latex/lshort-vietnamese/src/spec.tex
%doc %{_texmfdistdir}/doc/latex/lshort-vietnamese/src/things.tex
%doc %{_texmfdistdir}/doc/latex/lshort-vietnamese/src/tiengviet.tex
%doc %{_texmfdistdir}/doc/latex/lshort-vietnamese/src/title.tex
%doc %{_texmfdistdir}/doc/latex/lshort-vietnamese/src/typeset.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.00-2
+ Revision: 753549
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 4.00-1
+ Revision: 718908
- texlive-lshort-vietnamese
- texlive-lshort-vietnamese
- texlive-lshort-vietnamese
- texlive-lshort-vietnamese

