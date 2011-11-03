# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/crossreference
# catalog-date 2007-01-01 17:45:33 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-crossreference
Version:	20070101
Release:	1
Summary:	Crossreferences within documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/crossreference
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crossreference.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crossreference.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crossreference.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package defines cross-references (essentially 'grand' label
references), which may be listed in a table of cross-
references.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/crossreference/crossreference.sty
%doc %{_texmfdistdir}/doc/latex/crossreference/README
%doc %{_texmfdistdir}/doc/latex/crossreference/crossreference.pdf
%doc %{_texmfdistdir}/doc/latex/crossreference/xrefexample.tex
#- source
%doc %{_texmfdistdir}/source/latex/crossreference/crossreference.drv
%doc %{_texmfdistdir}/source/latex/crossreference/crossreference.dtx
%doc %{_texmfdistdir}/source/latex/crossreference/crossreference.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
