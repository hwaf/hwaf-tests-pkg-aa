#include <iostream>
#include "TH1D.h"

#include "pkg-aa/h1d.hh"

using namespace pkg_aa;

void test_th1d()
{
  TH1D *h = new TH1D("h1", "h1", 100, 0., 100.);
  std::cout << "h1: " << h->GetEntries() << "\n";
  delete h; h = NULL;
}
