import FWCore.ParameterSet.Config as cms

def customise(process):
	if hasattr(process.VtxSmeared,"X0"):
		VertexX = process.VtxSmeared.X0
		VertexY = process.VtxSmeared.Y0
		VertexZ = process.VtxSmeared.Z0

	if hasattr(process.VtxSmeared,"MeanX"):
		VertexX = process.VtxSmeared.MeanX
		VertexY = process.VtxSmeared.MeanY
		VertexZ = process.VtxSmeared.MeanZ


	
	process.load('SimTransport.HectorProducerForCTPPS.HectorTransport_cfi')
	process.LHCTransport.HectorForCTPPS.VtxMeanX  = VertexX
	process.LHCTransport.HectorForCTPPS.VtxMeanY  = VertexY
	process.LHCTransport.HectorForCTPPS.VtxMeanZ = VertexZ

	###################################
	process.load('FastSimulation.CTPPSSimHitProducer.CTPPSSimHitProducer_cfi')
	process.load('FastSimulation.CTPPSRecHitProducer.CTPPSRecHitProducer_cfi')
	process.load('FastSimulation.CTPPSFastTrackingProducer.CTPPSFastTrackingProducer_cfi')
	###################################
	process.mix.mixObjects.mixSH.crossingFrames.append('CTPPSHits')
	process.mix.mixObjects.mixSH.input.append(cms.InputTag("CTPPSSimHits","CTPPSHits"))
	process.mix.mixObjects.mixSH.subdets.append('CTPPSHits')
       
			
	# CTPPS simHit sequence 
	process.simulation_step.replace(process.psim,process.psim+process.CTPPSSimHits)
        # SimTransport on path
        process.transport_step = cms.Path(process.generator+process.LHCTransport)

	process.schedule.insert(2,process.transport_step)


	# output
    	outputModule = None
    	outdict = process.outputModules_()
    	if outdict.has_key("AODSIMoutput"):
	    process.AODSIMoutput.outputCommands.extend(cms.untracked.vstring('keep *_CTPPSSimHits_*_*','keep *_CTPPSFastRecHits_*_*'
,'keep *_CTPPSFastTracks_*_*'))
	    process.reconstruction_step.replace(process.reconstruction,process.reconstruction*process.CTPPSFastRecHits*process.CTPPSFastTracks) 	
    	elif outdict.has_key("FASTPUoutput"):
	    process.FASTPUoutput.outputCommands.extend(cms.untracked.vstring('keep *_CTPPSSimHits_*_*')) 	
			
	
	return(process)

