#ifndef DataFormats_CTPPSFastTracking_CTPPSFastTrackContainer_H
#define DataFormats_CTPPSFastTracking_CTPPSFastTrackContainer_H

#include "DataFormats/CTPPSFastTracking/interface/CTPPSFastTrack.h"
#include "DataFormats/Common/interface/Ref.h"
#include "DataFormats/Common/interface/RefProd.h"
#include <vector>
#include "DataFormats/Common/interface/RefToBase.h" 

namespace edm {
    typedef std::vector<CTPPSFastTrack> CTPPSFastTrackContainer;
} // edm

#endif 

