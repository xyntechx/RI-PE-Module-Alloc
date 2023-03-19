def raw_to_key(sport, gender):
    match sport:
        case "FOOTBALL (B)":
            return "FOOTBALL_B"
        case "FLOORBALL (B)":
            return "FLOORBALL_B"
        case "TENNIS (C)":
            if gender == "MALE":
                return "TENNIS_B"
            else:
                return "TENNIS_G"
        case "BADMINTON (C)":
            if gender == "MALE":
                return "BADMINTON_B"
            else:
                return "BADMINTON_G"
        case "HANDBALL (G)":
            return "HANDBALL_G"
        case "GROUP EXERCISE (G)":
            return "GROUP_EXERCISE_G"
        case "VOLLEYBALL (C)":
            if gender == "MALE":
                return "VOLLEYBALL_B"
            else:
                return "VOLLEYBALL_G"
        case "TABLE TENNIS (C)":
            if gender == "MALE":
                return "TABLE_TENNIS_B"
            else:
                return "TABLE_TENNIS_G"
        case "FRISBEE (G)":
            return "FRISBEE_G"
        case "PICKLE BALL (C)":
            if gender == "MALE":
                return "PICKLE_BALL_B"
            else:
                return "PICKLE_BALL_G"
        case "HANDBALL (B)":
            return "HANDBALL_B"
        case "BASKETBALL (B)":
            return "BASKETBALL_B"
        case "LACROSSE (G)":
            return "LACROSSE_G"
        case "FLOORBALL (G)":
            return "FLOORBALL_G"
        case "STREET NETBALL (G)":
            return "STREET_NETBALL_G"
        case "HOCKEY (B)":
            return "HOCKEY_B"
        case "FRISBEE (B)":
            return "FRISBEE_B"
        case "TCHOUKBALL (G)":
            return "TCHOUKBALL_G"
        case "BASKETBALL (G)":
            return "BASKETBALL_G"
        case "FIT AND FAB (G)":
            return "FIT_AND_FAB_G"
        case "TOUCH / TAG RUGBY (G)":
            return "TOUCH_TAG_RUGBY_G"
        case "BADMINTON (G)":
            return "BADMINTON_G"
        case "TENNIS (B)":
            return "TENNIS_B"
        case "FRISBEE (C)":
            if gender == "MALE":
                return "FRISBEE_B"
            else:
                return "FRISBEE_G"
