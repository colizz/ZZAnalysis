import FWCore.ParameterSet.Config as cms

from ZZAnalysis.SVFlavourTag.pfSVFlavourTagInfos_cfi import pfSVFlavourTagInfos
# from RecoBTag.ONNXRuntime.boostedJetONNXJetTagsProducer_cfi import boostedJetONNXJetTagsProducer
from ZZAnalysis.SVFlavourTag.pfSVFlavourONNXTagsProducer_cfi import pfSVFlavourONNXTagsProducer

pfParticleNetSVFlavourTagInfos = pfSVFlavourTagInfos.clone(
    deltar_match_sv_pfcand = 0.4,
    pf_candidates = "packedPFCandidates",
    secondary_vertices = "slimmedSecondaryVertices",
    vertices = "offlineSlimmedPrimaryVertices",
    debugMode = False,
)

pfParticleNetSVFlavourTagsPhantomJets =  pfSVFlavourONNXTagsProducer.clone(
    src = 'pfParticleNetSVFlavourTagInfos',
    jets = cms.InputTag('pfParticleNetSVFlavourTagInfos', 'svPhantomJets'),
    preprocess_json = 'ZZAnalysis/SVFlavourTag/data/ParticleNetSV/V01/preprocess_corr.json',
    model_path = 'ZZAnalysis/SVFlavourTag/data/ParticleNetSV/V01/model.onnx',
    flav_names = ['probb', 'probc', 'probcfromb', 'probl'],
    debugMode = False,
)
