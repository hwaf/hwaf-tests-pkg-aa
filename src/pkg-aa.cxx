#include <iostream>
#include "TH1D.h"

#include "pkg-aa/h1d.hh"

using namespace pkg_aa;

void test_h1d()
{
  TH1D *h = new TH1D("h1-aa", "h1-aa", 100, 0., 100.);
  std::cout << "h1-aa: " << h->GetEntries() << "\n";
  delete h; h = NULL;
}
