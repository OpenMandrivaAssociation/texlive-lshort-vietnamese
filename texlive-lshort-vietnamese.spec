%global tl_name lshort-vietnamese
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.00
Release:	%{tl_revision}.1
Summary:	Vietnamese version of the LaTeX introduction
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/vietnamese
License:	gpl2+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-vietnamese.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-vietnamese.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Vietnamese version of A Short Introduction to LaTeX2e.

