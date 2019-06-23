from collections import namedtuple

AssistLeaders = namedtuple("AssistLeaders", ["LeagueID", "PerMode", "PlayerOrTeam", "Season", "SeasonType"])

AssistTracker = namedtuple("AssistTracker", ["College", "Conference", "Country", "DataFrom", "DataTo", "Division",
                                             "DraftPick", "DraftYear", "GameScope", "Height", "LastNGames", "LeagueID",
                                             "Location", "Month", "OpponentTeamID", "Outcome", "POURound", "PerMode",
                                             "PlayerExperience", "PlayerPosition", "Season", "TeamID", "VsConference",
                                             "VsDivision", "Weight"])

BoxScoreAdvancedV2 = namedtuple("BoxScoreAdvancedV2", ["EndPeriod", "EndRange", "GameID", "StartPeriod", "StartRange"])

BoxScoreDefensive = namedtuple("BoxScoreDefensive", ["GameID"])

BoxScoreFourFactorsV2 = namedtuple("BoxScoreFourFactorsV2", ["EndPeriod", "EndRange", "GameID", "RangeType",
                                                             "StartPeriod", "StartRange"])

BoxScoreMatchups = namedtuple("BoxScoreMatchups", ["GameID"])

BoxScoreMiscV2 = namedtuple("BoxScoreMiscV2", ["EndPeriod", "EndRange", "GameID", "RangeType",
                                               "StartPeriod", "StartRange"])

BoxScorePlayerTrackV2 = namedtuple("BoxScorePlayerTrackV2", ["GameID"])

BoxScoreScoringV2 = namedtuple("BoxScoreScoringV2", ["EndPeriod", "EndRange", "GameID", "RangeType",
                                                     "StartPeriod", "StartRange"])

BoxScoreSummaryV2 = namedtuple("BoxScoreSummaryV2", ["GameID"])

BoxScoreTraditionalV2 = namedtuple("BoxScoreTraditionalV2", ["EndPeriod", "EndRange", "GameID", "RangeType",
                                                             "StartPeriod", "StartRange"])

BoxScoreUsageV2 = namedtuple("BoxScoreUsageV2", ["EndPeriod", "EndRange", "GameID", "RangeType",
                                                 "StartPeriod", "StartRange"])

CommonAllPlayers = namedtuple("CommonAllPlayers", ["IsOnlyCurrentSeason", "LeagueID", "Season"])

CommonPlayerInfo = namedtuple("CommonAllPlayers", ["LeagueID", "PlayerID"])

CommonPlayoffSeries = namedtuple("CommonPlayoffSeries", ["LeagueID", "PlayerID", "Season"])

CommonTeamRoster = namedtuple("CommonTeamRoster", ["LeagueID", "TeamID", "Season"])

CommonTeamYears = namedtuple("CommonTeamYears", ["LeagueID"])

DefenseHub = namedtuple("DefenseHub", ["GameScope", "LeagueID", "PlayerOrTeam", "PlayerScope", "Season", "SeasonType"])

DraftCombineDrillResults = namedtuple("DraftCombineDrillResults", ["LeagueID", "SeasonYear"])

DraftCombineNonStationaryShooting = namedtuple("DraftCombineNonStationaryShooting", ["LeagueID", "SeasonYear"])

DraftCombinePlayerAnthro = namedtuple("DraftCombinePlayerAnthro", ["LeagueID", "SeasonYear"])

DraftCombineSpotShooting = namedtuple("DraftCombineSpotShooting", ["LeagueID", "SeasonYear"])

DraftCombineStats = namedtuple("DraftCombineStats", ["LeagueID", "SeasonYear"])

DraftHistory = namedtuple("DraftHistory", ["LeagueID", "TopX", "TeamID", "Season", "RoundPick", "RoundNum",
                                           "OverallPick", "College"])

FantasyWidget = namedtuple("FantasyWidget", ["ActivePlayers", "LastNGames", "LeagueID", "Season", "SeasonType",
                                             "TodaysOpponent", "TodaysPlayers", "VsDivision", "VsConference", "TeamID",
                                             "SeasonSegment", "Position", "PlayerID", "PORound", "OpponentTeamID",
                                             "Month", "Location", "DateTo", "DateFrom"])

FranchiseHistory = namedtuple("FranchiseHistory", ["LeagueID"])

FranchiseLeaders = namedtuple("FranchiseLeaders", ["LeagueID", "TeamID"])

FranchisePlayers = namedtuple("FranchisePlayers", ["LeagueID", "TeamID", "PerMode", "SeasonType"])

HomePageLeaders = namedtuple("HomePageLeaders", ["GameScope", "LeagueID", "PlayerOrTeam", "PlayerScope", "Season",
                                                 "SeasonType", "StatCategory"])

HomePageV2 = namedtuple("HomePageV2", ["GameScope", "LeagueID", "PlayerOrTeam", "PlayerScope", "Season", "SeasonType",
                                       "StatType"])

InfographicFanDuelPlayer = namedtuple("InfographicFanDuelPlayer", ["GameID"])

LeadersTiles = namedtuple("LeadersTiles", ["GameScope", "LeagueID", "PlayerOrTeam", "PlayerScope", "Season",
                                           "SeasonType", "Stat"])

LeagueDashLineups = namedtuple("LeagueDashLineups", ["GroupQuantity", "LastNGames", "MeasureType", "Month",
                                                     "OpponentTeamID", "PaceAdjust", "PerMode", "PlusMinus", "Rank",
                                                     "Season", "SeasonType", "VsDivision", "VsConference", "TeamID",
                                                     "ShotClockRange", "SeasonSegment", "PORound",
                                                     "Outcome", "Location", "LeagueID", "GameSegment",
                                                     "Division", "DateTo", "DateFrom", "Conference"])

LeagueDashOppPtShot = namedtuple("LeagueDashOppPtShot", ["LeagueID", "PerMode", "Season", "SeasonType", "VsDivision",
                                                         "VsConference", "TouchTimeRange", "TeamID", "ShotDistRange",
                                                         "ShotClockRange", "SeasonSegment", "Period", "PRound",
                                                         "Outcome", "OpponentTeamID", "Month", "Location", "LastNGames",
                                                         "GeneralRange", "GameSegment", "DribbleRange", "Division",
                                                         "DateTo", "DateFrom", "Conference", "CloseDefDistRange"])

LeagueDashPlayerBioStats = namedtuple("LeagueDashPlayerBioStats", ["LeagueID", "PerMode", "Season", "SeasonType",
                                                                   "Weight", "VsDivision", "VsConference", "TeamID",
                                                                   "StarterBench", "ShotClockRange", "SeasonSegment",
                                                                   "PlayerPosition", "PlayerExperience", "Period",
                                                                   "PORound", "Outcome", "OpponentTeamID", "Month",
                                                                   "Location", "LastNGames", "Height", "GameSegment",
                                                                   "GameScope", "DraftYear", "DraftPick", "Division",
                                                                   "DateTo", "DateFrom", "Country", "Conference",
                                                                   "College"])

LeagueDashPlayerClutch = namedtuple("LeagueDashPlayerClutch", ["AheadBehind", "ClutchTime", "LastNGames", "MeasureType",
                                                               "Month", "OpponentTeamID", "PaceAdjust", "PerMode",
                                                               "Period", "PlusMinus", "PointDiff", "Rank", "Season",
                                                               "SeasonType", "Weight", "VsDivision", "VsConference",
                                                               "TeamID", "StarterBench", "ShotClockRange",
                                                               "SeasonSegment", "PlayerPosition", "PlayerExperience",
                                                               "PORound", "Outcome", "Location", "LeagueID",
                                                               "Height", "GameSegment", "GameScope",
                                                               "DraftYear", "DraftPick", "Division", "DateTo",
                                                               "DateFrom", "Country", "Conference", "College"])

LeagueDashTeamPtShot = namedtuple("LeagueDashTeamPtShot", ["LeagueID", "PerMode", "Season", "SeasonType", "VsDivision",
                                                           "VsConference", "TouchTimeRange", "TeamID", "ShotDistRange",
                                                           "ShotClockRange", "SeasonSegment", "Period", "PORound",
                                                           "Outcome", "OpponentTeamID", "Month", "Location",
                                                           "LastNGames", "GeneralRange", "GameSegment", "DribbleRange",
                                                           "Division", "DateTo", "DateFrom", "Conference",
                                                           "CloseDefDistRange"])

LeagueDashTeamShotLocations = namedtuple("LeagueDashTeamShotLocations", ["DistanceRange", "LastNGames", "MeasureType",
                                                                         "Month", "OpponentTeamID", "PaceAdjust",
                                                                         "PerMode", "Period", "PlusMInus", "Rank",
                                                                         "Season", "SeasonType", "VsDivision",
                                                                         "VsConference", "TeamID", "StarterBench",
                                                                         "ShotClockRange", "SeasonSegment",
                                                                         "PlayerPosition", "PlayerExperience",
                                                                         "PORound", "Outcome", "Location", "LeagueID",
                                                                         "GameSegment", "GameScope", "Division",
                                                                         "DateTo", "DateFrom", "Conference"])

LeagueDashPlayerStats = namedtuple("LeagueDashPlayerStats", ["LastNGames", "MeasureType", "Month", "OpponentTeamID",
                                                             "PaceAdjust", "PerMode", "Period", "PlusMinus", "Rank",
                                                             "Season", "SeasonType", "Weight", "VsDivision",
                                                             "VsConference", "TwoWay", "TeamID", "StarterBench",
                                                             "ShotClockRange", "SeasonSegment", "PlayerPosition",
                                                             "PlayerExperience", "PORound", "Outcome", "Location",
                                                             "LeagueID", "Height", "GameSegment", "GameScope",
                                                             "DraftYear", "DraftPick", "Division", "DateTo", "DateFrom",
                                                             "Country", "Conference", "College"])

LeagueDashPtDefend = namedtuple("LeagueDashPtDefend", ["DefenseCategory", "LeagueID", "PerMode", "Season", "SeasonType",
                                                       "Weight", "VsDivision", "VsConference", "TeamID", "StarterBench",
                                                       "SeasonSegment", "PlayerPosition", "PlayerID",
                                                       "PlayerExperience", "Period", "PORound", "Outcome",
                                                       "OpponentTeamID", "Month", "Location", "LastNGame", "Height",
                                                       "GameSegment", "DraftYear", "DraftPick", "Division", "DateTo",
                                                       "DateFrom", "Country", "Conference", "College"])

LeagueDashPtStats = namedtuple("LeagueDashPtStats", ["LastNGames", "Month", "OpponentTeamID", "PlayerOrTeam", "PerMode",
                                                     "PtMeasureType", "Season", "SeasonType", "Weight", "VsDivision",
                                                     "VsConference", "TeamID", "StarterBench",
                                                     "SeasonSegment", "PlayerPosition", "PlayerID", "PlayerExperience",
                                                     "PORound", "Outcome", "Location", "LeagueID", "Height",
                                                     "GameScope", "DraftYear", "DraftPick", "Division", "DateTo",
                                                     "DateFrom", "Country", "Conference", "College"])

LeagueDashPtTeamDefend = namedtuple("LeagueDashPtTeamDefend", ["LeagueID", "Season", "SeasonType", "VsDivision",
                                                               "VsConference", "TeamID", "SeasonSegment",
                                                               "Period", "PORound", "Outcome", "OpponentTeamID",
                                                               "Month", "Location", "LastNGame", "GameSegment",
                                                               "DateTo", "DateFrom", "Conference"])

LeagueDashTeamClutch = namedtuple("LeagueDashTeamClutch", ["AheadBehind", "ClutchTime", "LastNGames", "MeasureType",
                                                           "Month", "OpponentTeamID", "PaceAdjust", "PerMode", "Period",
                                                           "PlusMinus", "PointsDiff", "Rank", "Season", "SeasonType",
                                                           "VsDivision", "VsConference", "TeamID", "StarterBench",
                                                           "ShotClockRange", "SeasonSegment", "PlayerPosition",
                                                           "PlayerExperience", "PORound", "Outcome", "Location",
                                                           "LeagueID", "GameSegment", "GameScope", "Division",
                                                           "DateTo", "DateFrom", "Conference"])

LeagueDashTeamPtStats = namedtuple("LeagueDashTeamPtStats", ["LastNGames", "MeasureType", "Month", "OpponentTeamID",
                                                             "PaceAdjust", "PerMode", "Period", "PlusMinus", "Rank",
                                                             "Season", "SeasonType", "VsDivision", "VsConference",
                                                             "TwoWay", "TeamID", "StarterBEnch", "ShotClockRange",
                                                             "SeasonSegment", "PlayerPosition", "PlayerExperience",
                                                             "PORound", "Outcome", "Location", "LeagueID",
                                                             "GameSegment", "GameScope", "Division", "DateTo",
                                                             "DateFrom", "Conference"])

LeagueGameFinder = namedtuple("LeagueGameFinder", ["PlayerOrTeam", "YearsExperience", "VsTeamID", "VsDivision",
                                                   "VsConference", "TeamID", "StarterBench", "SeasonType",
                                                   "SeasonSegment", "Season", "RookieYear", "PlayerID", "PORound",
                                                   "Outcome", "LtTOV", "LtTD", "LtSTL", "LtREB", "LtPTS", "LtPF",
                                                   "LtOREB", "LtMINUTES", "LtFT_PCT", "LtFTM", "LtFTA", "LtFG_PCT",
                                                   "LtFGM", "LtFGA", "LtFG3_PCT", "LtFG3M", "LtFG3A", "LtDREB", "LtDD",
                                                   "LtBLK", "LtAST", "Location", "LeagueID", "GtTOV", "GtTD", "GtSTL",
                                                   "GtREB", "GtPTS", "GtPF", "GtOREB", "GtMINUTES", "GtFT_PCT", "GtFTM",
                                                   "GtFTA", "GtFG_PCT", "GtFGM", "GtFGA", "GtFG3_PCT", "GtFG3M",
                                                   "GtFG3A", "GtDREB", "GtDD", "GtBLK", "GtAST", "GameID", "EqTOV",
                                                   "EqTD", "EqSTL", "EqREB", "EqPTS", "EqPF", "EqOREB", "EqMINUTES",
                                                   "EqFT_PCT", "EqFTM", "EqFTA", "EqFG_PCT", "EqFGM", "EqFGA",
                                                   "EqFG3_PCT", "EqFG3M", "EqFG3A", "EqDREB", "EqDD", "EqBLK", "EqAST",
                                                   "DraftYear", "DraftTeamID", "DraftRound", "DraftNumber", "Division",
                                                   "DateTo", "DateFrom", "Conference"])

LeagueGameLog = namedtuple("LeagueGameLog", ["Counter", "Direction", "LeagueID", "PlayerOrTeam", "Season", "SeasonType",
                                             "Sorter", "DateTo", "DateFrom"])

LeagueLeaders = namedtuple("LeagueLeaders", ["LeagueID", "PerMode", "Scope", "Season", "SeasonType", "StatCategory",
                                             "ActiveFlag"])

LeaguePlayerOnDetails = namedtuple("LeaguePlayerOnDetails", ["LastNGames", "MeasureType", "Month", "OpponentTeamID",
                                                             "PaceAdjust", "PerMode", "Period", "PlusMinus", "Rank",
                                                             "Season", "SeasonType", "TeamID", "VsDivision",
                                                             "VsConference", "SeasonSegment", "Outcome", "Location",
                                                             "LeagueID", "GameSegment", "DateTo", "DateFrom"])

LeagueSeasonMatchups = namedtuple("LeagueSeasonMatchups", ["LeagueID", "Season", "SeasonType", "PerMode", "PORound",
                                                           "Outcome", "OffTeamID", "OffPlayerID", "DefTeamID",
                                                           "DefPlayerID", "DateTo", "DateFrom"])
LeagueStandings = namedtuple("LeagueStandings", ["LeagueID", "Season", "SeasonType", "SeasonYear"])

PlayByPlay = namedtuple("PlayByPlay", ["EndPeriod", "GameID", "StartPeriod"])

PlayByPlayV2 = namedtuple("PlayByPlayV2", ["EndPeriod", "GameID", "StartPeriod"])

PlayerAwards = namedtuple("PlayerAwards", ["PlayerID"])

PlayerCareerStats = namedtuple("PlayerCareerStats", ["PerMode", "PlayerID", "LeagueID"])

PlayerCompare = namedtuple("PlayerCompare", ["LastNGames", "MeasureType", "Month", "OpponentTeamID", "PaceAdjust",
                                             "PerMode", "Period", "PlayerIDList", "PlusMinus", "Rank", "Season",
                                             "SeasonType", "VsPlayerIDList", "VsDivision", "VsConference",
                                             "ShotClockRange", "SeasonSegment", "Outcome", "Location", "LeagueID",
                                             "GameSegment", "Division", "DateTo", "DateFrom", "Conference"])

PlayerDashboardByClutch = namedtuple("PlayerDashboardByClutch", ["LastNGames", "MeasureType", "Month", "OpponentTeamID",
                                                                 "PaceAdjust", "PerMode", "Period", "PlayerID",
                                                                 "PlusMinus", "Rank", "Season", "SeasonType",
                                                                 "VsDivision", "VsConference", "ShotClockRange",
                                                                 "SeasonSegment", "PORound", "Outcome", "Location",
                                                                 "LeagueID", "GameSegment", "DateTo", "DateFrom"])

PlayerDashboardByGameSplits = namedtuple("PlayerDashboardByGameSplits", ["LastNGames", "MeasureType", "Month",
                                                                         "OpponentTeamID", "PaceAdjust", "PerMode",
                                                                         "Period", "PlayerID", "PlusMinus", "Rank",
                                                                         "Season", "SeasonType", "VsDivision",
                                                                         "VsConference", "ShotClockRange",
                                                                         "SeasonSegment", "PORound", "Outcome",
                                                                         "Location", "LeagueID", "GameSegment",
                                                                         "DateTo", "DateFrom"])

PlayerDashboardByGeneralSplits = namedtuple("PlayerDashboardByGeneralSplits", ["LastNGames", "MeasureType", "Month",
                                                                               "OpponentTeamID", "PaceAdjust",
                                                                               "PerMode", "Period", "PlayerID",
                                                                               "PlusMinus", "Rank", "Season",
                                                                               "SeasonType", "VsDivision",
                                                                               "VsConference", "ShotClockRange",
                                                                               "SeasonSegment", "PORound", "Outcome",
                                                                               "Location", "LeagueID", "GameSegment",
                                                                               "DateTo", "DateFrom"])

PlayerDashboardByLastNGames = namedtuple("PlayerDashboardByLastNGames", ["LastNGames", "MeasureType", "Month",
                                                                         "OpponentTeamID", "PaceAdjust", "PerMode",
                                                                         "Period", "PlayerID", "PlusMinus", "Rank",
                                                                         "Season", "SeasonType", "VsDivision",
                                                                         "VsConference", "ShotClockRange",
                                                                         "SeasonSegment", "PORound", "Outcome",
                                                                         "Location", "LeagueID", "GameSegment",
                                                                         "DateTo", "DateFrom"])

PlayerDashboardByOpponent = namedtuple("PlayerDashboardByOpponent", ["LastNGames", "MeasureType", "Month",
                                                                     "OpponentTeamID", "PaceAdjust", "PerMode",
                                                                     "Period", "PlayerID", "PlusMinus", "Rank",
                                                                     "Season", "SeasonType", "VsDivision",
                                                                     "VsConference", "ShotClockRange", "SeasonSegment",
                                                                     "PORound", "Outcome", "Location", "LeagueID",
                                                                     "GameSegment", "DateTo", "DateFrom"])

PlayerDashboardByShootingSplits = namedtuple("PlayerDashboardByShootingSplits", ["LastNGames", "MeasureType", "Month",
                                                                                 "OpponentTeamID", "PaceAdjust",
                                                                                 "PerMode", "Period", "PlayerID",
                                                                                 "PlusMinus", "Rank", "Season",
                                                                                 "SeasonType", "VsDivision",
                                                                                 "VsConference", "ShotClockRange",
                                                                                 "SeasonSegment", "PORound", "Outcome",
                                                                                 "Location", "LeagueID", "GameSegment",
                                                                                 "DateTo", "DateFrom"])

PlayerDashboardByTeamPerformance = namedtuple("PlayerDashboardByTeamPerformance", ["LastNGames", "MeasureType", "Month",
                                                                                   "OpponentTeamID", "PaceAdjust",
                                                                                   "PerMode", "Period", "PlayerID",
                                                                                   "PlusMinus", "Rank", "Season",
                                                                                   "SeasonType", "VsDivision",
                                                                                   "VsConference", "ShotClockRange",
                                                                                   "SeasonSegment", "PORound",
                                                                                   "Outcome", "Location", "LeagueID",
                                                                                   "GameSegment", "DateTo", "DateFrom"])

PlayerDashboardByYearOverYear = namedtuple("PlayerDashboardByYearOverYear", ["LastNGames", "MeasureType", "Month",
                                                                             "OpponentTeamID", "PaceAdjust",
                                                                             "PerMode", "Period", "PlayerID",
                                                                             "PlusMinus", "Rank", "Season",
                                                                             "SeasonType", "VsDivision",
                                                                             "VsConference", "ShotClockRange",
                                                                             "SeasonSegment", "PORound",
                                                                             "Outcome", "Location", "LeagueID",
                                                                             "GameSegment", "DateTo", "DateFrom"])

PlayerDashPtPass = namedtuple("PlayerDashPtPass", ["LastNGames", "LeagueID", "Month", "OpponentTeamID", "PerMode",
                                                   "PlayerID", "Season", "SeasonType", "TeamID", "VsDivision",
                                                   "VsConference", "SeasonSegment", "Outcome", "Location", "DateTo",
                                                   "DateFrom"])

PlayerDashPtReb = namedtuple("PlayerDashPtReb", ["LastNGames", "LeagueID", "Month", "OpponentTeamID", "PerMode",
                                                 "PlayerID", "Season", "SeasonType", "TeamID", "VsDivision",
                                                 "VsConference", "SeasonSegment", "Outcome", "Location", "DateTo",
                                                 "DateFrom"])

PlayerDashPtShotDefend = namedtuple("PlayerDashPtShotDefend", ["LastNGames", "LeagueID", "Month", "OpponentTeamID",
                                                               "PerMode", "Period", "PlayerID", "Season", "SeasonType",
                                                               "TeamID", "VsDivision", "VsConference", "SeasonSegment",
                                                               "Outcome", "Location", "DateTo", "GameSegment",
                                                               "DateFrom"])

PlayerDashPtShots = namedtuple("PlayerDashPtShots", ["LastNGames", "LeagueID", "Month", "OpponentTeamID", "PerMode",
                                                     "Period", "PlayerID", "Season", "SeasonType", "TeamID",
                                                     "VsDivision", "VsConference", "SeasonSegment", "Outcome",
                                                     "Location", "DateTo", "GameeSegment", "DateFrom"])

PlayerFantasyProfile = namedtuple("PlayerFantasyProfile", ["MeasureType", "PaceAdjust", "PerMode", "PlayerID",
                                                           "PlusMinus", "Rank", "Season", "SeasonType", "LeagueID"])

PlayerFantasyProfileBarGraph = namedtuple("PlayerFantasyProfileBarGraph", ["PlayerID", "Season", "SeasonType",
                                                                           "LeagueID"])

PlayerGameLog = namedtuple("PlayerGameLog", ["PlayerID", "Season", "SeasonType", "LeagueID", "DateTo", "DateFrom"])

PlayerGameStreakFinder = namedtuple("PlayerGameStreakFinder", ["YearsExperience", "VsTeamID", "VsDivision",
                                                               "VsConference", "TeamID", "StarterBench", "SeasonType",
                                                               "SeasonSegment", "Season", "RookieYear", "PlayerID",
                                                               "PORound", "Outcome", "MinGames", "LtTOV", "LtTD",
                                                               "LtSTL", "LtREB", "LtPTS", "LtPF", "LtOREB", "LtMINUTES",
                                                               "LtFT_PCT", "LtFTM", "LtFTA", "LtFG_PCT", "LtFGM",
                                                               "LtFGA", "LtFG3_PCT", "LtFG3M", "LtFG3A", "LtDREB",
                                                               "LtDD", "LtBLK", "LtAST", "Location", "LeagueID",
                                                               "GtTOV", "GtTD", "GtSTL", "GtREB", "GtPTS", "GtPF",
                                                               "GtOREB", "GtMINUTES", "GtFT_PCT", "GtFTM", "GtFTA",
                                                               "GtFG_PCT", "GtFGM", "GtFGA", "GtFG3_PCT", "GtFG3M",
                                                               "GtFG3A", "GtDREB", "GtDD", "GtBLK", "GtAST", "GameID",
                                                               "EqTOV", "EqTD", "EqSTL", "EqREB", "EqPTS", "EqPF",
                                                               "EqOREB", "EqMINUTES", "EqFT_PCT", "EqFTM", "EqFTA",
                                                               "EqFG_PCT", "EqFGM", "EqFGA", "EqFG3_PCT", "EqFG3M",
                                                               "EqFG3A", "EqDREB", "EqDD", "EqBLK", "EqAST",
                                                               "DraftYear", "DraftTeamID", "DraftRound", "DraftNumber",
                                                               "Division", "DateTo", "DateFrom", "Conference",
                                                               "ActiveStreaksOnly"])

PlayerNextNGames = namedtuple("PlayerNextNGames", ["NumberOfGames", "PlayerID", "Season", "SeasonType", "LeagueID"])

PlayerProfileV2 = namedtuple("PlayerProfileV2", ["PerMode", "PlayerID", "LeagueID"])

PlayerVsPlayer = namedtuple("PlayerVsPlayer", ["LastNGames", "MeasureType", "Month", "OpponentTeamID", "PaceAdjust",
                                               "PerMode", "Period", "PlayerID", "PlusMinus", "Rank", "Season",
                                               "SeasonType", "VsPlayerID", "VsDivision", "VsConference",
                                               "SeasonSegment", "Outcome", "Location", "LeagueID", "GameSegment",
                                               "DateTo", "DateFrom"])

PlayoffPicture = namedtuple("PlayoffPicture", ["LeagueID", "SeasonID"])

Scoreboard = namedtuple("Scoreboard", ["DayOffset", "GameDate", "LeagueID"])

ScoreboardV2 = namedtuple("ScoreboardV2", ["DayOffset", "GameDate", "LeagueID"])

ShotChartDetail = namedtuple("ShotChartDetail", ["ContextMeasure", "LastNGames", "LeagueID", "Month", "OpponentTeamID",
                                                 "Period", "PlayerID", "SeasonType", "TeamID", "VsDivision",
                                                 "VsConference", "StartRange", "StartPeriod", "SeasonSegment",
                                                 "Season", "RookieYear", "RangeType", "Position", "PointDiff",
                                                 "PlayerPosition", "Outcome", "Location", "GameSegment", "GameID",
                                                 "EndRange", "EndPeriod", "DateTo", "DateFrom", "ContextFilter",
                                                 "ClutchTime", "AheadBehind"])

ShotChartLineupDetail = namedtuple("ShotChartLineupDetail", ["ContextMeasure", "GROUP_ID", "LeagueID", "Period",
                                                             "Season", "SeasonType", "VsDivision", "VsConference",
                                                             "TeamID", "SeasonSegment", "Outcome", "OpponentTeamID",
                                                             "Month", "Location", "LastNGames", "GameSegment", "GameID",
                                                             "DateTo", "DateFrom", "ContextFilter"])

SynergyPlayTypes = namedtuple("SynergyPlayTypes", ["LeagueID", "PerMode", "playerOrTeam", "SeasonType", "SeasonYear",
                                                   "TypeGrouping", "PlayType"])

TeamAndPlayersVsPlayers = namedtuple("TeamAndPlayersVsPlayers", ["LastNGames", "MeasureType", "Month", "OpponentTeamID",
                                                                 "PaceAdjust", "PerMode", "Period", "PlayerID1",
                                                                 "PlayerID2", "PlayerID3", "PlayerID4", "PlayerID5",
                                                                 "PlusMinus", "Rank", "Season", "SeasonType", "TeamID",
                                                                 "VsPlayerID1", "VsPlayerID2", "VsPlayerID3",
                                                                 "VsPlayerID4", "VsPlayerID5", "VsTeamID", "VsDivision",
                                                                 "VsConference", "ShotClockRange", "SeasonSegment",
                                                                 "Outcome", "Location", "LeagueID", "GameSegment",
                                                                 "Division", "DateTo", "DateFrom", "Conference"])

TeamDashboardByClutch = namedtuple("TeamDashboardByClutch", ["LastNGames", "MeasureType", "Month", "OpponentTeamID",
                                                             "PaceAdjust", "PerMode", "Period", "PlusMinus", "Rank",
                                                             "Season", "SeasonType", "TeamID", "VsDivision",
                                                             "VsConference", "ShotClockRange", "SeasonSegment",
                                                             "PORound", "Outcome", "Location", "LeagueID",
                                                             "GameSegment", "DateTo", "DateFrom"])

TeamDashboardByGameSplits = namedtuple("TeamDashboardByGameSplits", ["LastNGames", "MeasureType", "Month",
                                                                     "OpponentTeamID", "PaceAdjust", "PerMode",
                                                                     "Period", "PlusMinus", "Rank", "Season",
                                                                     "SeasonType", "TeamID", "VsDivision",
                                                                     "VsConference", "ShotClockRange", "SeasonSegment",
                                                                     "PORound", "Outcome", "Location", "LeagueID",
                                                                     "GameSegment", "DateTo", "DateFrom"])

TeamDashboardByGeneralSplits = namedtuple("TeamDashboardByGeneralSplits", ["LastNGames", "MeasureType", "Month",
                                                                           "OpponentTeamID", "PaceAdjust", "PerMode",
                                                                           "Period", "PlusMinus", "Rank", "Season",
                                                                           "SeasonType", "TeamID", "VsDivision",
                                                                           "VsConference", "ShotClockRange",
                                                                           "SeasonSegment", "PORound", "Outcome",
                                                                           "Location", "LeagueID", "GameSegment",
                                                                           "DateTo", "DateFrom"])

TeamDashboardByLastNGames = namedtuple("TeamDashboardByLastNGames", ["LastNGames", "MeasureType", "Month",
                                                                     "OpponentTeamID", "PaceAdjust", "PerMode",
                                                                     "Period", "PlusMinus", "Rank", "Season",
                                                                     "SeasonType", "TeamID", "VsDivision",
                                                                     "VsConference", "ShotClockRange", "SeasonSegment",
                                                                     "PORound", "Outcome", "Location", "LeagueID",
                                                                     "GameSegment", "DateTo", "DateFrom"])

TeamDashboardByOpponent = namedtuple("TeamDashboardByOpponent", ["LastNGames", "MeasureType", "Month", "OpponentTeamID",
                                                                 "PaceAdjust", "PerMode", "Period", "PlusMinus", "Rank",
                                                                 "Season", "SeasonType", "TeamID", "VsDivision",
                                                                 "VsConference", "ShotClockRange", "SeasonSegment",
                                                                 "PORound", "Outcome", "Location", "LeagueID",
                                                                 "GameSegment", "DateTo", "DateFrom"])

TeamDashboardByShootingSplits = namedtuple("TeamDashboardByShootingSplits", ["LastNGames", "MeasureType", "Month",
                                                                             "OpponentTeamID", "PaceAdjust", "PerMode",
                                                                             "Period", "PlusMinus", "Rank", "Season",
                                                                             "SeasonType", "TeamID", "VsDivision",
                                                                             "VsConference", "ShotClockRange",
                                                                             "SeasonSegment", "PORound", "Outcome",
                                                                             "Location", "LeagueID", "GameSegment",
                                                                             "DateTo", "DateFrom"])

TeamDashboardByTeamPerformance = namedtuple("TeamDashboardByTeamPerformance", ["LastNGames", "MeasureType", "Month",
                                                                               "OpponentTeamID", "PaceAdjust",
                                                                               "PerMode", "Period", "PlusMinus", "Rank",
                                                                               "Season", "SeasonType", "TeamID",
                                                                               "VsDivision", "VsConference",
                                                                               "ShotClockRange", "SeasonSegment",
                                                                               "PORound", "Outcome", "Location",
                                                                               "LeagueID", "GameSegment", "DateTo",
                                                                               "DateFrom"])

TeamDashboardByYearOverYear = namedtuple("TeamDashboardByYearOverYear", ["LastNGames", "MeasureType", "Month",
                                                                         "OpponentTeamID", "PaceAdjust", "PerMode",
                                                                         "Period", "PlusMinus", "Rank", "Season",
                                                                         "SeasonType", "TeamID", "VsDivision",
                                                                         "VsConference", "ShotClockRange",
                                                                         "SeasonSegment", "PORound", "Outcome",
                                                                         "Location", "LeagueID", "GameSegment",
                                                                         "DateTo", "DateFrom"])

TeamDashLineups = namedtuple("TeamDashLineups", ["GroupQuantity", "LastNGames", "MeasureType", "Month",
                                                 "OpponentTeamID", "PaceAdjust", "PerMode", "Period", "PlusMinus",
                                                 "Rank", "Season", "SeasonType", "TeamID", "VsDivision", "VsConference",
                                                 "ShotClockRange", "SeasonSegment", "PORound", "Outcome", "Location",
                                                 "LeagueID", "GameSegment", "GameID", "DateTo", "DateFrom"])

TeamDashPtPass = namedtuple("TeamDashPtPass", ["LastNGames", "LeagueID", "Month", "OpponentTeamID", "PerMode", "Season",
                                               "SeasonType", "TeamID", "VsDivision", "VsConference", "SeasonSegment",
                                               "Outcome", "Location", "DateTo", "DateFrom"])

TeamDashPtReb = namedtuple("TeamDashPtReb", ["LastNGames", "LeagueID", "Month", "OpponentTeamID", "PerMode", "Period",
                                             "Season", "SeasonType", "TeamID", "VsDivision", "VsConference",
                                             "SeasonSegment", "Outcome", "Location", "GameSegment", "DateTo",
                                             "DateFrom"])

TeamDashPtShots = namedtuple("TeamDashPtShots", ["LastNGames", "LeagueID", "Month", "OpponentTeamID", "PerMode",
                                                 "Period", "Season", "SeasonType", "TeamID", "VsDivision",
                                                 "VsConference", "SeasonSegment", "Outcome", "Location",
                                                 "GameSegment", "DateTo", "DateFrom"])

TeamDetails = namedtuple("TeamDetails", ["TeamID"])

TeamGameLog = namedtuple("TeamGameLog", ["TeamID", "Season", "SeasonType", "LeagueID", "DateTo", "DateFrom"])

TeamGameStreakFinder = namedtuple("TeamGameStreakFinder", ["WrsOPPTOV", "WrsOPPSTL", "WrsOPPREB", "WrsOPPPTSPAINT",
                                                           "WrsOPPPTSOFFTOV", "WrsOPPPTSFB", "WrsOPPPTS2NDCHANCE",
                                                           "WrsOPPPTS", "WrsOPPPF", "WrsOPPOREB", "WrsOPPFT_PCT",
                                                           "WrsOPPFTM", "WrsOPPFTA", "WrsOPPFG_PCT", "WrsOPPFGM",
                                                           "WrsOPPFGA", "WrsOPPFG3PCT", "WrsOPPFG3M", "WrsOPPFG3A",
                                                           "WrsOPPDREB", "WrsOPPBLK", "WrsOPPAST", "WStreak",
                                                           "VsTeamID", "VsDivision", "VsConference", "TeamID",
                                                           "SeasonType", "SeasonSegment", "Season", "PORound",
                                                           "Outcome", "MinGames", "LtTOV", "LtTD", "LtSTL", "LtREB",
                                                           "LtPTSPAINT", "LtPTSOFFTOV", "LtPTSFB", "LtPTS2NDCHANCE",
                                                           "LtPTS", "LtPF", "LtOREB", "LtOPPTOV", "LtOPPSTL",
                                                           "LtOPPREB", "LtOPPPTSPAINT", "LtOPPPTSOFFTOV", "LtOPPPTSFB",
                                                           "LtOPPPTS2NDCHANCE", "LtOPPPTS", "LtOPPPF", "LtOPPOREB",
                                                           "LtOPPFT_PCT", "LtOPPFTM", "LtOPPFTA", "LtOPPFG_PCT",
                                                           "LtOPPFGM", "LtOPPFGA", "LtOPPFG3PCT", "LtOPPFG3M",
                                                           "LtOPPFG3A", "LtOPPDREB", "LtOPPBLK", "LtOPPAST",
                                                           "LtMINUTES", "LtFT_PCT", "LtFTM", "LtFTA", "LtFG_PCT",
                                                           "LtFGM", "LtFGA", "LtFG3_PCT", "LtFG3M", "LtFG3A", "LtDREB",
                                                           "LtDD", "LtBLK", "LtAST", "Location", "LeagueID", "LStreak",
                                                           "GtTOV", "GtTD", "GtSTL", "GtREB", "GtPTSPAINT",
                                                           "GtPTSOFFTOV", "GtPTSFB", "GtPTS2NDCHANCE", "GtPTS", "GtPF",
                                                           "GtOREB", "GtOPPTOV", "GtOPPSTL", "GtOPPREB",
                                                           "GtOPPPTSPAINT", "GtOPPPTSOFFTOV", "GtOPPPTSFB",
                                                           "GtOPPPTS2NDCHANCE", "GtOPPPTS", "GtOPPPF", "GtOPPOREB",
                                                           "GtOPPFT_PCT", "GtOPPFTM", "GtOPPFTA", "GtOPPFG_PCT",
                                                           "GtOPPFGM", "GtOPPFGA", "GtOPPFG3PCT", "GtOPPFG3M",
                                                           "GtOPPFG3A", "GtOPPDREB", "GtOPPBLK", "GtOPPAST",
                                                           "GtMINUTES", "GtFT_PCT", "GtFTM", "GtFTA", "GtFG_PCT",
                                                           "GtFGM", "GtFGA", "GtFG3_PCT", "GtFG3M", "GtFG3A", "GtDREB",
                                                           "GtDD", "GtBLK", "GtAST", "GameID", "EqTOV", "EqTD", "EqSTL",
                                                           "EqREB", "EqPTSPAINT", "EqPTSOFFTOV", "EqPTSFB",
                                                           "EqPTS2NDCHANCE", "EqPTS", "EqPF", "EqOREB", "EqOPPPTSPAINT",
                                                           "EqOPPPTSOFFTOV", "EqOPPPTSFB", "EqOPPPTS2NDCHANCE",
                                                           "EqMINUTES", "EqFT_PCT", "EqFTM", "EqFTA", "EqFG_PCT",
                                                           "EqFGM", "EqFGA", "EqFG3_PCT", "EqFG3M", "EqFG3A", "EqDREB",
                                                           "EqDD", "EqBLK", "EqAST", "Division", "DateTo", "DateFrom",
                                                           "Conference", "BtrOPPTOV", "BtrOPPSTL", "BtrOPPREB",
                                                           "BtrOPPPTSPAINT", "BtrOPPPTSOFFTOV", "BtrOPPPTSFB",
                                                           "BtrOPPPTS2NDCHANCE", "BtrOPPPTS", "BtrOPPPF", "BtrOPPOREB",
                                                           "BtrOPPFT_PCT", "BtrOPPFTM", "BtrOPPFTA", "BtrOPPFG_PCT",
                                                           "BtrOPPFGM", "BtrOPPFGA", "BtrOPPFG3PCT", "BtrOPPFG3M",
                                                           "BtrOPPFG3A", "BtrOPPDREB", "BtrOPPBLK", "BtrOPPAST",
                                                           "ActiveTeamsOnly", "ActiveStreaksOnly"])

TeamHistoricalLeaders = namedtuple("TeamHistoricalLeaders", ["LeagueID", "SeasonID", "TeamID"])

TeamInfoCommon = namedtuple("TeamInfoCommon", ["LeagueID", "TeamID", "SeasonType", "Season"])

TeamPlayerDashboard = namedtuple("TeamPlayerDashboard", ["LastNGames", "MeasureType", "Month", "OpponentTeamID",
                                                         "PaceAdjust", "PerMode", "Period", "PlusMinus", "Rank",
                                                         "Season", "SeasonType", "TeamID", "VsDivision", "VsConference",
                                                         "ShotClockRange", "SeasonSegment", "PORound", "Outcome",
                                                         "Location", "LeagueID", "GameSegment", "DateTo", "DateFrom"])

TeamPlayerOnOffDetails = namedtuple("TeamPlayerOnOffDetails", ["LastNGames", "MeasureType", "Month", "OpponentTeamID",
                                                               "PaceAdjust", "PerMode", "Period", "PlusMinus", "Rank",
                                                               "Season", "SeasonType", "TeamID", "VsDivision",
                                                               "VsConference", "SeasonSegment", "Outcome", "Location",
                                                               "LeagueID", "GameSegment", "DateTo", "DateFrom"])

TeamPlayerOnOffSummary = namedtuple("TeamPlayerOnOffSummary", ["LastNGames", "MeasureType", "Month", "OpponentTeamID",
                                                               "PaceAdjust", "PerMode", "Period", "PlusMinus", "Rank",
                                                               "Season", "SeasonType", "TeamID", "VsDivision",
                                                               "VsConference", "SeasonSegment", "Outcome", "Location",
                                                               "LeagueID", "GameSegment", "DateTo", "DateFrom"])

TeamVsPlayer = namedtuple("TeamVsPlayer", ["LastNGames", "MeasureType", "Month", "OpponentTeamID", "PaceAdjust",
                                           "PerMode", "Period", "PlusMinus", "Rank", "Season", "SeasonType", "TeamID",
                                           "VsPlayerID", "VsDivision", "VsConference", "SeasonSegment", "PlayerID",
                                           "Outcome", "Location", "LeagueID", "GameSegment", "DateTo", "DateFrom"])

TeamYearByYearStats = namedtuple("TeamYearByYearStats", ["LeagueID", "PerMode", "SeasonType", "TeamID"])

VideoDetails = namedtuple("VideoDetails", ["ContextMeasure", "LastNGames", "Month", "OpponentTeamID", "Period",
                                           "PlayerID", "Season", "SeasonType", "TeamID", "VsDivision", "VsConference",
                                           "StartRange", "StartPeriod", "SeasonSegment", "RookieYear", "RangeType",
                                           "Position", "PointDiff", "Outcome", "Location", "LeagueID", "GameSegment",
                                           "GameID", "EndRange", "EndPeriod", "DateTo", "DateFrom", "ContextFilter",
                                           "ClutchTime", "AheadBehind"])

VideoEvents = namedtuple("VideoEvents", ["GameEventID", "GameID"])

VideoStatus = namedtuple("VideoStatus", ["GameDate", "LeagueID"])

WinProbabilityPBP = namedtuple("WinProbabilityPBP", ["GameID", "RunType"])
