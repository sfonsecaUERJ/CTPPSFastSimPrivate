#include "DataFormats/CTPPSFastTracking/interface/CTPPSFastTrack.h"
#include "DataFormats/CTPPSFastTracking/interface/CTPPSFastTrackContainer.h"
#include "DataFormats/Common/interface/Wrapper.h"

namespace DataFormats_CTPPSFastTracking {
    struct dictionary {
        CTPPSFastTrack xxxx;
	edm::CTPPSFastTrackContainer sxxxx;
        edm::Wrapper<edm::CTPPSFastTrackContainer> dummy1;
	std::vector<const CTPPSFastTrack*> dummy2;
    };
}   
