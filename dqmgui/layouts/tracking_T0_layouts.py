def trackinglayout(i, p, *rows): i["Tracking/Layouts/" + p] = DQMItem(layout=rows)

trackinglayout(dqmitems, "01 - Tracking ReportSummary",
   [{ 'path': "Tracking/EventInfo/reportSummaryMap",
      'description': " Quality Test results plotted for Tracking parameters : Chi2, TrackRate, #of Hits in Track - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "no" }},
    { 'path': "Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/GoodTracksFractionVsLS_GenTk",
      'description': "Good fraction of tracks vs Lumisections", 'draw': { 'withref': "no" }},
    { 'path': "Tracking/TrackParameters/generalTracks/GeneralProperties/TrackEtaPhi_ImpactPoint_GenTk",
      'description': "Number of tracks (color scale) as function of eta and phi of the tracks", 'draw': { 'withref': "no" }}])
trackinglayout(dqmitems, "02a - Tracks (pp collisions)",
   [{ 'path': "Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/NumberOfTracks_GenTk",
      'description': "Number of Reconstructed Tracks with high purity selection and pt > 1 GeV - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
    { 'path': "Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/NumberOfRecHitsPerTrack_GenTk",
      'description': "Number of RecHits per Track with high purity selection and pt > 1 GeV  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
    { 'path': "Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/TrackPt_ImpactPoint_GenTk",
      'description': "Pt of Reconstructed Track with high purity selection and pt > 1 GeV  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}],
   [{ 'path': "Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/Chi2oNDF_GenTk",
      'description': "Chi Square per DoF with high purity selection and pt > 1 GeV  -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
    { 'path': "Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/TrackPhi_ImpactPoint_GenTk",
      'description': "Phi distribution of Reconstructed Tracks with high purity selection and pt > 1 GeV -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
    { 'path': "Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/TrackEta_ImpactPoint_GenTk",
      'description': " Eta distribution of Reconstructed Tracks with high purity selection and pt > 1 GeV - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}])
trackinglayout(dqmitems, "02b - Total Hits Strip and Pixel (pp collisions)",
   [{ 'path': "Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/Strip/NumberOfRecHitsPerTrack_Strip_GenTk",
      'description': "Number of Strip valid RecHits in each Track", 'draw': { 'withref': "yes" }},
    { 'path': "Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/Pixel/NumberOfRecHitsPerTrack_Pixel_GenTk",
      'description': "Number of Pixel valid RecHits in each Track", 'draw': { 'withref': "yes" }},
    { 'path': "Tracking/TrackParameters/highPurityTracks/pt_1/HitEffFromHitPattern/globalEfficiencies",
      'description': "Global efficiency for each subdetector", 'draw': { 'withref': "yes" }}])
trackinglayout(dqmitems, "03 - Tracks (Cosmic Tracking)",
   [{ 'path': "Tracking/TrackParameters/GeneralProperties/NumberOfTracks_CKFTk",
                'description': "Number of Reconstructed Tracks - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
    { 'path': "Tracking/TrackParameters/HitProperties/NumberOfRecHitsPerTrack_CKFTk",
      'description': "Number of RecHits per Track  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
    { 'path': "Tracking/TrackParameters/GeneralProperties/TrackPt_CKFTk",
      'description': "Pt of Reconstructed Track  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}],
   [{ 'path': "Tracking/TrackParameters/GeneralProperties/Chi2oNDF_CKFTk",
      'description': "Chi Sqare per DoF  -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
    { 'path': "Tracking/TrackParameters/GeneralProperties/TrackPhi_CKFTk",
      'description': "Phi distribution of Reconstructed Tracks -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
    { 'path': "Tracking/TrackParameters/GeneralProperties/TrackEta_CKFTk",
      'description': " Eta distribution of Reconstructed Tracks - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}])
trackinglayout(dqmitems, "04 - Tracking vs LS",
   [{ 'path': "Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/GoodTracksFractionVsLS_GenTk",
      'description': "Fraction of tracks versus Lumi Section", 'draw': { 'withref': "yes" }}],
   [{ 'path': "Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/NumberOfRecHitsPerTrackVsLS_GenTk",
      'description': "Number of rec hits per track vs LS", 'draw': { 'withref': "yes" }}])
trackinglayout(dqmitems, "05 - Number of Seeds (pp collisions)",
   [{ 'path': "Tracking/TrackParameters/generalTracks/TrackBuilding/NumberOfSeeds_initialStepSeeds_initialStep",
      'description': "Number of Seed in tracking iteration 0 (no entry: ERROR) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
    { 'path': "Tracking/TrackParameters/generalTracks/TrackBuilding/NumberOfSeeds_lowPtTripletStepSeeds_lowPtTripletStep",
      'description': "Number of Seed in tracking iteration 1 (no entry: ERROR) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
    { 'path': "Tracking/TrackParameters/generalTracks/TrackBuilding/NumberOfSeeds_pixelPairStepSeeds_pixelPairStep",
      'description': "Number of Seed in tracking iteration 2 (no entry: ERROR) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
    { 'path': "Tracking/TrackParameters/generalTracks/TrackBuilding/NumberOfSeeds_detachedTripletStepSeeds_detachedTripletStep",
      'description': "Number of Seed in tracking iteration 3 (no entry: ERROR) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}],
   [{ 'path': "Tracking/TrackParameters/generalTracks/TrackBuilding/NumberOfSeeds_mixedTripletStepSeeds_mixedTripletStep",
      'description': "Number of Seed in tracking iteration 4 (no entry: ERROR) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
    { 'path': "Tracking/TrackParameters/generalTracks/TrackBuilding/NumberOfSeeds_pixelLessStepSeeds_pixelLessStep",
      'description': "Number of Seed in tracking iteration 5 (no entry: ERROR) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
    { 'path': "Tracking/TrackParameters/generalTracks/TrackBuilding/NumberOfSeeds_tobTecStepSeeds_tobTecStep",
      'description': "Number of Seed in tracking iteration 6 (no entry: ERROR) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}])
trackinglayout(dqmitems, "06 - Tracks resolution",
    [{'path': "Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/DistanceOfClosestApproachToBS_GenTk",
      'description': "Distance in the XY plane between the track and the Beam spot"},
    { 'path': "Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/DistanceOfClosestApproachToBSdz_GenTk",
     'description': "Distance in the Z axis between the track and the Beam spot"},
    {'path': "Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/DistanceOfClosestApproachToBSVsPhi_GenTk",
      'description': "Distance in the XY plane between the track and the Beam spot versus phi"},
    { 'path': "Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/DistanceOfClosestApproachToBSVsEta_GenTk",
      'description': "Distance in the XY plane between the track and the Beam spot versus eta"}],
   [{ 'path': "Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/TrackQoverP_ImpactPoint_GenTk",
     'description': "Charge over momentum"},
   { 'path': "Tracking/TrackParameters/generalTracks/GeneralProperties/Quality_GenTk",
     'description': "Tracks for different quality flags"},
   { 'path': "Tracking/TrackParameters/generalTracks/GeneralProperties/NumberofTracks_Hardvtx_GenTk",
     'description': "matched the Hard vertex"},
   { 'path': "Tracking/TrackParameters/generalTracks/GeneralProperties/NumberOfTracks_PUvtx_GenTk",
     'description': "matched a PU vertex"}])
trackinglayout(dqmitems, "06a - Tracks quality",
   [{'path': "Tracking/TrackParameters/generalTracks/GeneralProperties/TrackPtHighPurity_ImpactPoint_GenTk",
     'description': "Distance in the XY plane between the track and the Beam spot"},
   { 'path': "Tracking/TrackParameters/generalTracks/GeneralProperties/TrackPtTight_ImpactPoint_GenTk",
     'description': "Distance in the XY plane between the track and the Beam spot versus phi"},
   { 'path': "Tracking/TrackParameters/generalTracks/GeneralProperties/TrackPtLoose_ImpactPoint_GenTk",
     'description': "Distance in the XY plane between the track and the Beam spot versus eta"}],
  [{ 'path': "Tracking/TrackParameters/generalTracks/GeneralProperties/TrackEtaHighpurity_ImpactPoint_GenTk",
     'description': "Distance in the XY plane between the track and the Beam spot"},
   { 'path': "Tracking/TrackParameters/generalTracks/GeneralProperties/TrackEtaTight_ImpactPoint_GenTk",
     'description': "Distance in the XY plane between the track and the Beam spot versus phi"},
   { 'path': "Tracking/TrackParameters/generalTracks/GeneralProperties/TrackEtaLoose_ImpactPoint_GenTk",
     'description': "Distance in the XY plane between the track and the Beam spot versus eta"}])
trackinglayout(dqmitems, "07 - Vertex reconstruction",
  [{ 'path': "Tracking/PrimaryVertices/highPurityTracks/pt_0to1/offline/NumberOfGoodPVtx_offline",
     'description': "Number of Good Primary Vertices"},
   { 'path': "Tracking/PrimaryVertices/highPurityTracks/pt_0to1/offline/GoodPVtxNumberOfTracks_offline",
     'description': "Number of Good Tracks per Vertex"},
   { 'path': "Tracking/TrackParameters/generalTracks/GeneralProperties/NumberofTracks_Hardvtx_PUvtx_GenTk",
     'description': "the number of tracks per vertex, for the hard vertex and for others PU vertices"}],
  [{ 'path': "OfflinePV/offlinePrimaryVertices/tagDiffX",
     'description': "Difference between PV and beamspot in x-direction"},
   { 'path': "OfflinePV/offlinePrimaryVertices/tagDiffY",
     'description': "Difference between PV and beamspot in y-direction"},
   { 'path': "Tracking/PrimaryVertices/highPurityTracks/pt_0to1/offline/FractionOfGoodPVtx_offline",
     'description': "Fraction of Good Primary Vertices"}])
trackinglayout(dqmitems, "08 - Tracking Efficiency",
  [{ 'path': "Tracking/TrackParameters/generalTracks/GeneralProperties/TkEtaPhi_Ratio_byFoldingmap_ImpactPoint_GenTk",
     'description': "Efficiency from folding method using the relative difference"},
   { 'path': "Tracking/TrackParameters/generalTracks/GeneralProperties/TkEtaPhi_RelativeDifference_byFoldingmap_ImpactPoint_GenTk",
     'description': "Efficiency from folding method using the ratio"},
   { 'path': "Tracking/TrackParameters/generalTracks/GeneralProperties/Ratio_byFolding_ImpactPoint_GenTk",
     'description': "Tracking Efficiency"}],
  [{ 'path': "Tracking/TrackParameters/generalTracks/GeneralProperties/TkEtaPhi_Ratio_byFoldingmap_op_ImpactPoint_GenTk",
     'description': "Efficiency from folding method(2) using the relative difference"},
   { 'path': "Tracking/TrackParameters/generalTracks/GeneralProperties/TkEtaPhi_RelativeDifference_byFoldingmap_op_ImpactPoint_GenTk",
     'description': "Efficiency from folding method(2) using the ratio"},
   { 'path': "Tracking/TrackParameters/generalTracks/GeneralProperties/Ratio_byFolding2_ImpactPoint_GenTk",
     'description': "Tracking Efficiency (2)"}])
trackinglayout(dqmitems, "09 - Beam Monitor",
  [{ 'path': "AlcaBeamMonitor/Validation/hxLumibased PrimaryVertex-DataBase",
     'description': ""},
   { 'path': "AlcaBeamMonitor/Validation/hyLumibased PrimaryVertex-DataBase",
     'description': ""},
   { 'path': "AlcaBeamMonitor/Validation/hzLumibased PrimaryVertex-DataBase",
     'description': ""}],
  [{ 'path': "AlcaBeamMonitor/Debug/hsigmaXLumibased PrimaryVertex-DataBase fit",
     'description': ""},
    { 'path': "AlcaBeamMonitor/Debug/hsigmaYLumibased PrimaryVertex-DataBase fit",
     'description': ""},
    { 'path': "AlcaBeamMonitor/Debug/hsigmaZLumibased PrimaryVertex-DataBase fit",
     'description': ""}
   ])
trackinglayout(dqmitems, "10 - Tracks (HI run)",
 [{ 'path': "Tracking/TrackParameters/GeneralProperties/NumberOfTracks_HeavyIonTk",
    'description': "Number of Reconstructed Tracks - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/HitProperties/NumberOfRecHitsPerTrack_HeavyIonTk",
    'description': "Number of RecHits per Track  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/GeneralProperties/TrackPt_ImpactPoint_HeavyIonTk",
    'description': "Pt of Reconstructed Track  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}],
 [{ 'path': "Tracking/TrackParameters/GeneralProperties/Chi2oNDF_HeavyIonTk",
    'description': "Chi Sqare per DoF  -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/GeneralProperties/TrackPhi_ImpactPoint_HeavyIonTk",
    'description': "Phi distribution of Reconstructed Tracks -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/GeneralProperties/TrackEta_ImpactPoint_HeavyIonTk",
    'description': " Eta distribution of Reconstructed Tracks - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}])
trackinglayout(dqmitems, "11 - Short Tracks Resolution",
 [{ 'path': "Tracking/ShortTrackResolution/trackPt3lAllPt",
    'description': "pT resolution of shortened tracks - 3 layers", 'draw': { 'withref': "no" }},
  { 'path': "Tracking/ShortTrackResolution/trackPt4lAllPt",
    'description': "pT resolution of shortened tracks - 4 layers", 'draw': { 'withref': "no" }},
  { 'path': "Tracking/ShortTrackResolution/trackPt5lAllPt",
    'description': "pT resolution of shortened tracks - 5 layers", 'draw': { 'withref': "no" }}],
 [{ 'path': "Tracking/ShortTrackResolution/trackPt6lAllPt",
    'description': "pT resolution of shortened tracks - 6 layers", 'draw': { 'withref': "no" }},
  { 'path': "Tracking/ShortTrackResolution/trackPt7lAllPt",
    'description': "pT resolution of shortened tracks - 7 layers", 'draw': { 'withref': "no" }},
  { 'path': "Tracking/ShortTrackResolution/trackPt8lAllPt",
    'description': "pT resolution of shortened tracks - 8 layers", 'draw': { 'withref': "no" }}])
