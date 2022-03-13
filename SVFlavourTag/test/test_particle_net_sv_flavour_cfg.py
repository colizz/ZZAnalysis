import FWCore.ParameterSet.Config as cms

from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing('analysis')
options.inputFiles = 'file:/eos/cms/store/cmst3/group/vhcc/hc/samples/GluGluHToZZTo4L_M125_TuneCP5_13TeV_amcatnlo_JHUGenV714_herwig7/UL2018_v1/220306_114214/0000/step6_1.root'
options.maxEvents = 10
options.parseArguments()

process = cms.Process("PATtest")

## MessageLogger
# process.load("FWCore.MessageLogger.MessageLogger_cfi")
# process.MessageLogger.cerr.FwkReport.reportEvery = 100


## Options and Output Report
# process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

## Source
process.source = cms.Source("PoolSource",
    fileNames=cms.untracked.vstring(options.inputFiles)
)
## Maximal Number of Events
process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(options.maxEvents))


## Geometry and Detector Conditions (needed for a few patTuple production steps)
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2017_realistic')
process.load("Configuration.StandardSequences.MagneticField_cff")
# from TrackingTools.TransientTrack.TransientTrackBuilder_cfi import TransientTrackBuilderESProducer
process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)
process.load("ZZAnalysis.SVFlavourTag.pfParticleNetSVFlavourTagSuite_cff")
process.p = cms.Path(process.pfParticleNetSVFlavourTagInfos + process.pfParticleNetSVFlavourTagsPhantomJets)

## Output Module Configuration (expects a path 'p')
from PhysicsTools.PatAlgos.patEventContent_cff import patEventContentNoCleaning
process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('patTuple.root'),
                            #    outputCommands = cms.untracked.vstring('drop *', *patEventContentNoCleaning )
                               outputCommands = cms.untracked.vstring()
                               )

process.out.outputCommands.append('keep *_pfParticleNetSVFlavourTagInfos_*_*')
process.out.outputCommands.append('keep *_pfParticleNetSVFlavourTagInfos__*')
process.outpath = cms.EndPath(process.out)