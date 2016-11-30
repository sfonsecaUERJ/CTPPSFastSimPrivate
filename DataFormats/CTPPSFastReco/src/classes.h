#include "DataFormats/CTPPSFastReco/interface/CTPPSFastRecHit.h"
#include "DataFormats/CTPPSFastReco/interface/CTPPSFastRecHitContainer.h"
#include "DataFormats/Common/interface/Wrapper.h"

namespace DataFormats_CTPPSReco {
    struct dictionary {
        CTPPSFastRecHit xxxx;
	edm::CTPPSFastRecHitContainer sxxxx;
        edm::Wrapper<edm::CTPPSFastRecHitContainer> dummy1;
	std::vector<const CTPPSFastRecHit*> dummy2;
    };
}   
