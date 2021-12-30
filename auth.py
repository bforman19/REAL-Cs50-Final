from flask import Blueprint, Flask, redirect, render_template, flash, request, redirect, url_for
import os
import random

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")

@auth.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':

        image_file= url_for('static', filename='pictures/Unknown.png')
        x= "hello"
        
        warm_shooting = [{"url": "https://www.youtube.com/embed/tZocxBsONqY?start=120&end=128", "title": "Spin and Fire", "description": "Go 3 yards away from the goal on the wing, and begin with your back to the net. With a ball in your stick outstretched, swing your inside leg towards the goal and shoot the ball.", "reps": "12 each side"},
        {"url": "https://www.youtube.com/embed/tZocxBsONqY?start=183&end=199", "title": "Pop and Shoot", "description": "Go 3 yards away from the goal on the wing, and pop away from the net, taking three steps away from the net. On your last step load your back foot, and then explode into a step down shot.", "reps": "12 each side"},
        {"url": "https://www.youtube.com/embed/nJeWuDnikww?start=220&end=226", "title": "On the Run Warmups", "description": "Go 5 yards away from the goal on the wing, and lightly run towards the middle, taking an on the run shot. Goal is to hit offside low", "reps": "10 each side"},
        {"url": "https://www.youtube.com/embed/eUzj3EhPBS4?start=250&end=260", "title": "Facing the Net One Hand Top of the Stick Releases", "description": "With your body towards the goal, with one hand at the top of the stick, practice releasing the ball", "reps": "10 each side"},
        {"url": "https://www.youtube.com/embed/eUzj3EhPBS4?start=337&end=347", "title": "Kneeling Down Fires", "description": "In Front of the net, with one hand on the stick, load the ball. Then, bring your second to the stick, load, and fire.", "reps": "10 each side"},
        {"url": "https://www.youtube.com/embed/eUzj3EhPBS4?start=495&end=505", "title": "Standing Fires", "description": "In Front of the net, with one hand on the stick, load the ball. Then, bring your second to the stick, load, and fire.", "reps": "10 each side"},
        {"url": "https://www.youtube.com/embed/SGSYx_hbTS0?start=138&end=143", "title": "Power Shooting", "description": "With your body facing sidways, load your stick as far back as you can away from the net. With your legs planted, and your weight slightly shifted onto your back foot, explode towards the net and rotate your core along with your arms. Focus more on generating power versus accuracy.", "reps": "12 each side"},
        {"url": "https://www.youtube.com/embed/eUzj3EhPBS4?start=900&end=910", "title": "Sideways One Hand Shots", "description": "Sidways in Front of the net, with one hand on the stick, load the ball. Keep your one hand as far back as possible. Then load and fire.", "reps": "10 each side"}]
        
        wall_ball = [{"url": "https://www.youtube.com/embed/jCP5ze6OyKw?start=51&end=58", "title": "Overhand Wall Ball", "description": "With an overhand release, pass the ball against the wall, trying to aim for the same spot every time.", "reps": "50 each side"},
            {"url": "https://www.youtube.com/embed/jCP5ze6OyKw?start=98&end=105", "title": "Across Your body", "description": "With an overhand release, pass the ball against the wall. Try to aim so that the ball will cross over to your other hand, so that way it will make it harder for you to catch.", "reps": "50 each side"},
           
            {"url": "https://www.youtube.com/embed/jCP5ze6OyKw?start=135&end=142", "title": "One Hand Catches", "description": "With an overhand release, pass the ball against the wall, trying to aim so that the ball goes across your body. Then, instead of catching it two hands, catch with one.", "reps": "50 each side"},
          
            {"url": "https://www.youtube.com/embed/jCP5ze6OyKw?start=160&end=167", "title": "BTB Throws", "description": "Bring the stick behind your head, and release BTB, or behind the back, snapping your thumb towards your ear.", "reps": "50 each side"},
         
            {"url": "https://www.youtube.com/embed/jCP5ze6OyKw?start=227&end=235", "title": "Quicksticks", "description": "With your hands chocked up on the stick a little, release the ball overhand but instead of cradling when you catch, go right into your next throw.", "reps": "50 each side"},
          
            {"url": "https://www.youtube.com/embed/jCP5ze6OyKw?start=267&end=275", "title": "Switch Quicksticks", "description": "With your hands chocked up on the stick a little, release the ball overhand but instead of cradling when you catch, go right into your next throw. With switch quicksticks, pass the ball to the opposite side of your body that it was previously on.", "reps": "50 each side"},
         
            {"url": "https://www.youtube.com/embed/jCP5ze6OyKw?start=300&end=310", "title": "Pass with a fake", "description": "With an overhand release, pass the ball against the wall, trying to aim for the same spot every time. When you catch, give a fake to the wall, reload, then release the ball again.", "reps": "50 each side"},
            
            {"url": "https://www.youtube.com/embed/jCP5ze6OyKw?start=334&end=340", "title": "Sidearm release drill", "description": "With a sidearm release, pass the ball against the wall, trying to aim for the same spot every time.", "reps": "50 each side"},

            {"url": "https://www.youtube.com/embed/fLQhNF0nHaU?start=59&end=64", "title": "Catch and Split", "description": "With a overhand release, pass the ball against the wall. Once you catch the ball, switch hands. Then repeat this process on the other hand", "reps": "50 each side"},

            {"url": "https://www.youtube.com/embed/fLQhNF0nHaU?start=200&end=210", "title": "Catch and Switch", "description": "With a overhand release, pass the ball against the wall, and as you catch, switch hands. Then repeat this process on the other hand", "reps": "50 each side"},

            {"url": "https://www.youtube.com/embed/e1FbwWyvEIo?start=0&end=14", "title": "Two Ball wall ball", "description": "Play overhand catch with two balls against the wall. This might take time to master, but challenge yourself.", "reps": "2.5 min each side"},

            {"url": "https://www.youtube.com/embed/TiRdo2Bqwao?start=107&end=115", "title": "One Hand Throw and Catch", "description": "With one hand on the stick throw overhand balls against the wall, catching with one hand too.", "reps": "50 each side"},

            {"url": "https://www.youtube.com/embed/TiRdo2Bqwao?start=125&end=135", "title": "BTB to Around the World", "description": "Throw a Behind the back pass at the wall. When you catch, throw it around the world. Repeat this process.", "reps": "50 each side"},

            {"url": "https://www.youtube.com/embed/eUzj3EhPBS4?start=658&end=666", "title": "Kneeling One Hand", "description": "Kneeling down, with one hand high on the stick, throw overhand passes on the wall.", "reps": "50 each side"},

            {"url": "https://www.youtube.com/embed/eUzj3EhPBS4?start=680&end=690", "title": "Kneeling Two Hands", "description": "Kneeling down, with both hands on the stick, throw overhand quicksticks on the wall. Try to do this without cradles.", "reps": "50 each side"},

            {"url": "https://www.youtube.com/embed/eUzj3EhPBS4?start=755&end=765", "title": "Far away passes", "description": "Standing 15-20 feet away from the wall, throw overhand passes. Try to not have to move, working on your accurarcy.", "reps": "50 each side"},

            {"url": "https://www.youtube.com/embed/eUzj3EhPBS4?start=875&end=885", "title": "Load and Fires Wall Ball", "description": "Standing 10-15ft away from the wall, pop away taking three steps away from the wall. On your last step load your back foot, and then explode into a step down throw. This should be hard.", "reps": "25 each side"},

            {"url": "https://www.youtube.com/embed/eUzj3EhPBS4?start=1045&end=1055", "title": "Face dodge to Canadian", "description": "Standing 10-15ft away from the wall, face dodge, step through, and throw the ball canadian style against the wall. This means bringing your stick across your body and passing from there.", "reps": "25 each side"},

            {"url": "https://www.youtube.com/embed/3AUOWXtkxsA?start=311&end=321", "title": "Canandian Quicksticks", "description": "Throw the ball canadian style against the wall. This means bringing your stick across your body and passing from there. Instead of cradling, however, mkae this process quicksticks instead.", "reps": "25 each side"},

            {"url": "https://www.youtube.com/embed/3AUOWXtkxsA?start=344&end=354", "title": "Alternating Canandian Quicksticks", "description": "Throw the ball canadian style against the wall. This means bringing your stick across your body and passing from there. After throwing, catch the ball regular and quickstick it back. Then catch it Canadian, and repeat the process.", "reps": "25 each side: one rep is catching Canadian and Regular"},

            {"url": "https://www.youtube.com/embed/3AUOWXtkxsA?start=825&end=835", "title": "One Hand Canadians", "description": "With only one hand, throw the ball canadian style against the wall. This means bringing your stick across your body and passing from there.", "reps": "2.5 min each side"},

            {"url": "https://www.youtube.com/embed/3AUOWXtkxsA?start=882&end=892", "title": "Lever Passes", "description": "With the stick low in your body position, move the stick like a lever as the ball releases from your hands. We keep the stick low to try and recreate an in game situation.", "reps": "50 each side"},

            {"url": "https://www.youtube.com/embed/3AUOWXtkxsA?start=1003&end=1013", "title": "Face Dodge to Shovel", "description": "Face dodge with your stick, and as you carry it across your body, shovel the ball against the wall.", "reps": "25 each side"},

            {"url": "https://www.youtube.com/embed/3AUOWXtkxsA?start=1100&end=1110", "title": "Passing While Running", "description": "While passing the ball overhand against the wall, begin continiously running a few strides fowards and then backwards.", "reps": "50 each side"},
 
            {"url": "https://www.youtube.com/embed/3AUOWXtkxsA?start=1160&end=1170", "title": "Step Away Drill", "description": "While standing 10 feet away from the wall, have your stick up in a passing position, then bounce away as if your are evading a defender. Then make a pass to the wall, catch, and repeat on the other side.", "reps": "50 in total"},

            {"url": "https://www.youtube.com/embed/3AUOWXtkxsA?start=1237&end=1247", "title": "Split and Look Back", "description": "While standing 10 feet away from the wall, make a horizontal split dodge. Then make a fake with your stick as if you are looking back to a teamate behind you. After the fake, make a real pass to the wall, and repeat on the other side.", "reps": "50 in total"},
    
            {"url": "https://www.youtube.com/embed/3AUOWXtkxsA?start=1300&end=1310", "title": "Question Mark Practice", "description": "Standing with your back to the wall, punch with your outside hand, rolling yourself back towards the net. As this happens, switch hands. Then make a pass while running. This drill helps practice your question mark.", "reps": "50 in total"},

            {"url": "https://www.youtube.com/embed/3AUOWXtkxsA?start=1345&end=1355", "title": "Stepback Throwback", "description": "Standing with your back to the wall, begin backpadelling. Then, open yourself up to the wall, and throw the ball with the same hand you began the drill with.", "reps": "50 in total"}]


        no_ball = [{"url": "https://www.youtube.com/embed/CSnJYMIkhFY?start=34&end=42", "title": "Three Cone Dodging", "description": "Put three cones zizgaged 10 yards away from the net. Explode out of a dodge from the farthest cone, and split dodge your way through the cones. After the last cone, take an on the run shot aiming for far pipe.", "reps": "5 each side"},
        {"url": "https://www.youtube.com/embed/lJiBEVuFOgw?start=70&end=93", "title": "No stick Cradling", "description": "Without a stick, take a ball and begin to mimick the cradling movement with the ball in your hands. After a couple sets you begin to move as you perform this movement.", "reps": "30s each side for 4 sets"},
        {"url": "https://www.youtube.com/embed/MsnwIXJXllo?start=126&end=140", "title": "ZigZag Drill", "description": "Can be performed with or without resistance band. Set out 6 cones in a zigzag format. Starting from one end of the cone, split your way through the barriers as quickly as possible, taking little jab steps when you reach each cone.", "reps": "10 reps"},
        {"url": "https://www.youtube.com/embed/1P_4Fx467PU?start=12&end=44", "title": "Z Drill", "description": "with 8 cones zigzaged in front of you, begin chopping your feet as you aproach the first cone. With the stick in either hand, jab your foot at the cone and fake your stick in the direction of the cone. Afterwards, go back to chopping your feet and repeat the process at each cone.", "reps": "10 reps"},
        {"url": "https://www.youtube.com/embed/qtwKIxyOdGk?start=186&end=196", "title": "Ground Ball", "description": "Can be performed with or without a helper. Standing a few yards away from a ball, aproach the ball and get your knuckles to the ground as you scoop through the ball and cradle once you have it in your stick.", "reps": "20 reps each hand"},
        {"url": "https://www.youtube.com/embed/S7xJti9m1uw?start=73&end=90", "title": "4 Way Sprint", "description": "Set up Four Cones 8 yards apart. Sprint from one to the next, creating a square with your movement. Try to hug the cones as much as possible.", "reps": "6 reps each direction."},
        {"url": "https://www.youtube.com/embed/S7xJti9m1uw?start=110&end=120", "title": "Backpedal, shuffle, sprint.", "description": "Set up Four Cones 8 yards apart. Backpadel from the first to the second, side shuffel from the second to the third, and sprint from the 3rd to the 4th.", "reps": "6 reps each direction."},
        {"url": "https://www.youtube.com/embed/S7xJti9m1uw?start=170&end=180", "title": "X Drill", "description": "Set up Four Cones 8 yards apart in a square. Try to make an X with your movement. Sprint from one cone straight ahead. Then sprint diagonally across. Then Sprint foward. Then sprint diagonally, and you should end up where you started.", "reps": "6 reps each direction."},
        {"url": "https://www.youtube.com/embed/S7xJti9m1uw?start=184&end=194", "title": "Pro Agility Shuffel", "description": "Set up 3 Cones 5 yards apart in a straight line. From a few yards away from the middle cone, jog towards the center. Then, sprint, when you reach the cone, sprint in one direction, touch the cone, sprint back 10 yards, touch that cone, then finish in the middle.", "reps": "6 reps each direction."},
        {"url": "https://www.youtube.com/embed/qtwKIxyOdGk?start=50&end=57", "title": "Ground Ball No Stick", "description": "Can be performed with or without a helper. Standing a few yards away from a ball, aproach the ball and get your knuckles to the ground as you mimick a ground ball. Pick up the ball with both hands and explode through the ball as you regain your posture.", "reps": "30 reps"},
        {"url": "https://www.youtube.com/embed/FYJJbwG_i8U?start=25&end=40", "title": "Jump Squates", "description": "In a squat position, explode up and aim to touch the sky as you jump. Then, when you land, try to minimize the amount of time on the floor.", "reps": "5 sets of 10 jumps"},
        {"url": "https://www.youtube.com/embed/5CTD5BtSWTE?start=6&end=30", "title": "One Hand Cradling Drill", "description": "Set up two cones 10 yards apart. With one hand cradling, sprint towards one cone. When you get there, plant your foot and switch hands, all the while protecting your stick.", "reps": "10, alternating which hand goes first"},
        {"url": "https://www.youtube.com/embed/OvwOzQzHL88?start=120&end=130", "title": "Box Cradling", "description": "Running in a box-like motion, begin cradling the ball with both hands. You want to make your box relativley large, around 10 meters in side length. As you run each side of the box, you can alternate between jogging and sprinting, changing depending on which side of the box you're on.", "reps": "10 each side"},
        {"url": "https://www.youtube.com/embed/OvwOzQzHL88?start=180&end=200", "title": "Ground Ball Drill", "description": "Roll the ball out a couple feet in front of you, get your knees down, and scoop through the ball. One you pick it up, rise up and begin cradling. Then repeat the process", "reps": "40 each hand"},
        {"url": "https://www.youtube.com/embed/DsFEBk1vQ8c?start=207&end=230", "title": "Box Cradling Drill", "description": "Set up 4 cones in a square around 5 yards apart. Cradle fowards with one hand, switch when you get to the top cone and begin side shuffling with your opposite hand. Then backpedal back, and when you reach the last cone switch back to your original hand and shuffle to the starting cone.", "reps": "10 each side"},
        {"url": "https://www.youtube.com/embed/DsFEBk1vQ8c?start=350&end=375", "title": "Split Complex", "description": "Set up cones in a box formation, while also putting one in the middle. Then, sprint towards the middle cone, and split dodge towards the second one in the box. Then split dodge the second one and return back to the middle, repeating the process until you end up at the first cone.", "reps": "8 each side"},
        {"url": "https://www.youtube.com/embed/DsFEBk1vQ8c?start=420&end=446", "title": "Break the Double", "description": "Set up cones in a box formation, 5 yards apart, with one cone in the middle. Run up towards the top cone, switch hands when you get there and then side shuffel diagionally backwards. After that, aproach the other top cone, switch hands again, and side shuffel diagionally back to the original cone.", "reps": "8 each side"},
        {"url": "https://www.youtube.com/embed/wKZrODozLbc?start=35&end=40", "title": "Butt end catches", "description": "With one hand toss the ball up in the air, and try to hit it with the butt end of your stick. Repeat this process without letting the ball drop.", "reps": "40 each side"},
        {"url": "https://www.youtube.com/embed/wKZrODozLbc?start=60&end=70", "title": "Shaft Around Ball", "description": "Toss the ball up, and try to circle your shaft around the ball without letting them touch. Then catch the ball and repeat.", "reps": "25 each side"},
        {"url": "https://www.youtube.com/embed/wKZrODozLbc?start=80&end=90", "title": "Catch on the sidewall", "description": "Pop the ball up, and catch it on your sidewall of the head. Then throw it back in your pocket, and repeat the process.", "reps": "25 succesful catches each side"},
        {"url": "https://www.youtube.com/embed/wKZrODozLbc?start=90&end=100", "title": "Stick Twirls", "description": "Have two hands on your stick. With your top hand doing most of the work twirl your stick making it do revolutions in the air. Then try to catch it without having the ball drop.", "reps": "25 succesful twirls each side"},
        {"url": "https://www.youtube.com/embed/ekH0PolAKMI?start=25&end=50", "title": "Sidwall Spins", "description": "With the ball on the sidwall of your head, spin around in a circle while keeping the ball on the head. You will have to angle your shaft higher as you speed up.", "reps": "20 spins each side"},
        {"url": "https://www.youtube.com/embed/53X5vZLVFrw?start=20&end=120", "title": "Fire Feet Jabs", "description": "Setting up two sets of parrellel cones, one a bit longer than the other, begin pounding your feet. Then, with one foot going around the clock of the cones begin jabbing it fowards. After every jab return back to your feet moving in place.", "reps": "12 each foot"},
        {"url": "https://www.youtube.com/embed/Fd709C2uQYA?start=281&end=294", "title": "Shuffling Drill", "description": "With four cones(does not have to be chairs) placed in a line, shuffle through them, zigzaging through each layer. When you get to the top, zigzag backwards. When you reach the bottom, circle around and sprint throught the top.", "reps": "10"},
        {"url": "https://www.youtube.com/embed/Fd709C2uQYA?start=347&end=390", "title": "Shuttle Runs", "description": "With 50 yards as your length, sprint 4 times(there back there back) as your first rep. Then go to 5 lengths, then 6, then 7.", "reps": "1 set of drill"}]

        # {"url": "https://www.youtube.com/embed/ekH0PolAKMI?start=25&end=50", "title": "", "description": "", "reps": ""},





        little_ball = [{"url": "https://www.youtube.com/embed/DsH3Ym_7e8k?start=70&end=80", "title": "Low Angle Shooting", "description": "with balls at Gle, positition your body upfield. Make one or two fakes towards the net and finish in a corner.", "reps": "8 each side"},
                {"url": "https://www.youtube.com/embed/ocHH2x9xlUI?start=257&end=266", "title": "Split to Face Dodge", "description": "Starting at X, split dodge upfield and make your way a few yards past GLE. Then bounce out as if you are going to pass, and face dodge back towards the net. Shoot towards the net with your stick protected.", "reps": "8 each side"},
                {"url": "https://www.youtube.com/embed/lxAQwwTIYMI?start=42&end=50", "title": "One Handed BTBs", "description": "With both knees down and chest up, extend your stick with your outside arm. Then snap your thumb to your ear and release the ball behind your head, or BTB.", "reps": "10 each side"},
                {"url": "https://www.youtube.com/embed/lxAQwwTIYMI?start=155&end=202", "title": "Two Handed BTBs", "description": "With both knees down and chest up, extend your stick with both arms. Then snap your thumb to your ear and release the ball behind your head, or BTB.", "reps": "10 each side"},
                {"url": "https://www.youtube.com/embed/ezr2-t-O3mA?start=36&end=60", "title": "Inside Roll", "description": "Starting at GLE, 4 yards away from the goal, aproach topside with one hand on the stick. Then, 5 yards upfield, inside roll back towards the net and finish with your stick protected.", "reps": "10 each side"},
                {"url": "https://www.youtube.com/embed/ezr2-t-O3mA?start=60&end=76", "title": "Question Mark", "description": "Starting at GLE, 4 yards away from the goal, aproach topside with one hand on the stick. Then, 5 yards upfield, punch your stick to the outside and get both hands on the stick as you pivoting to the sideline. Flip your hips back towards the goal, and shoot.", "reps": "10 each side"},
                {"url": "https://www.youtube.com/embed/nJeWuDnikww?start=342&end=262", "title": "Alley dodge into tight finish", "description": "Go 10-12 yards away from the goal on the wing, and dodge towards X. Instead of going behind the goal, come across it and finish in front.", "reps": "8 each side"},
                {"url": "https://www.youtube.com/embed/nJ7_LepBOpU?start=50&end=60", "title": "Turn and bury", "description": "Starting at GLE, 4 yards away from the goal, aproach topside with one hand on the stick. One or two yards upfield, turn your hips and bury the ball. Make sure to look where you shooting so you can place the ball more accuractly.", "reps": "12 each side"},
                {"url": "https://www.youtube.com/embed/t18hqY74HgU?start=0&end=10", "title": "Zig Zag from X", "description": "Set out three cones behind the goal in a zig zag format. Starting at X, 10 yards behind the goal, aproach the lowest cone. When you get there, roll back towards the middle and repeat this process with cones 2 and 3. After the 3rd cone, continue past the middle and curl around the crease going into a topside finish.", "reps": "6 each side"},
                {"url": "https://www.youtube.com/embed/ezr2-t-O3mA?start=103&end=120", "title": "Rocker Step", "description": "Starting at GLE, 4 yards away from the goal, aproach topside with one hand on the stick. Then, 5 yards upfield, chop your feet and fake your hips as if you were gonna do an inside roll. Instead, continue upfield and curl into your shot.", "reps": "10 each side"},
                {"url": "https://www.youtube.com/embed/fZEpCXz_1xk?start=95&end=110", "title": "Redodge Drill", "description": "Starting at the box, set up cones in displayed matter. Dodge down either alley, bounce when you hit the last cone, and redodge down the same way. Inside finish around the crease", "reps": "10 each side"},
                {"url": "https://www.youtube.com/embed/DfCqclX8TBQ?start=29&end=45", "title": "Split Roll Hesi", "description": "Starting at X, make a split dodge, roll, hesitate, then finish topside", "reps": "8 each side"},
                {"url": "https://www.youtube.com/embed/DfCqclX8TBQ?start=90&end=105", "title": "Split Roll Hesi Jumpshot", "description": "Starting at X, make a split dodge, roll, hesitate, then finish with a jump shot topside", "reps": "8 each side"},
                {"url": "https://www.youtube.com/embed/YWRRQAJN9hQ?start=137&end=147", "title": "Swat the Fly", "description": "Can be performed with or without a feeder. Standing 2 yards away from the net, with a ball in your stick, extend outside hand out with your feet facing sideways. Load your back foot and snap your wrist towards the goal, shooting as hard as you can with 1 hand. Focus more on power and less on accuracy.", "reps": "10 reps"},
                {"url": "https://www.youtube.com/embed/fK2eyiM5vTM?start=152&end=105", "title": "Finalizer", "description": "Starting at X, make a split dodge, roll, finish come back to your original hand and finish around the net", "reps": "8 each side"}]


        shooting = [{"url": "https://www.youtube.com/embed/6B9y-aQa0Hs?start=40&end=50", "title": "Step Downs", "description": "Go 8 yards away from the goal on the wing, and put down a cone. If by yourself, start with a ball, take two shuffles back, and redistribute your weight into a shot. With a partner shuffle back without ball and get a pass into your shot.", "reps": "8 each side"}, 
        {"url": "https://www.youtube.com/embed/6B9y-aQa0Hs?start=125&end=137", "title": "Step Split Hitches", "description": "Start at the top edges, and go into a 3 shot cycle. 1st shot is a step down, second shot is a topside hitch, and a third is a split down the alley.", "reps": "3 cycles each side"}, 
        {"url": "https://www.youtube.com/embed/TDqpPM_dx88?start=158&end=168", "title": "Split into Crow Hop", "description": "Start at the top edges, switch hands, and try to take a big crow hop into a shot. Aim low corners. Switch the side of the field for your other hand.", "reps": "10 each side"}, 
        {"url": "https://www.youtube.com/embed/TDqpPM_dx88?start=195&end=206", "title": "Down the Alleys", "description": "Start at the top. While keeping the stick in your outside hand, and explode down the alley while taking an on the run shot. Try to aim opposite pipe.", "reps": "8 each side"}, 
        {"url": "https://www.youtube.com/embed/TDqpPM_dx88?start=232&end=240", "title": "Split Middles", "description": "Start at the top edges, split to the middle, and take an on the run shot. Try to aim opposite pipe.", "reps": "8 each side"},
        {"url": "https://www.youtube.com/embed/tZocxBsONqY?start=244&end=252", "title": "Layup Shooting", "description": "Go 8 yards in front of the goal, and start with your feet planted towards the net. With just your outside hand on the stick, explode towards the wing and take a shot on the run.", "reps": "10 each side"},
        {"url": "https://www.youtube.com/embed/tZocxBsONqY?start=330&end=338", "title": "Hitch Shooting", "description": "Go to the wing, take a hitch, and either take an on the run shot topside or a stepdown shot.", "reps": "8 each side"},
        {"url": "https://www.youtube.com/embed/tZocxBsONqY?start=340&end=345", "title": "Face Dodges", "description": "Go to the wing, take a crow hop into a face dodge, and finish running towards the goal. Remember to keep your stick protected as you run.", "reps": "8 each side"},
        {"url": "https://www.youtube.com/embed/tZocxBsONqY?start=360&end=366", "title": "Hitch andn Split", "description": "Go to the wing, take a crow hop into a hitch, take one step topside, and plant your feet. Then, split back down the alley and take an on the run shot", "reps": "8 each side"},
        {"url": "https://www.youtube.com/embed/tZocxBsONqY?start=404&end=410", "title": "Game Splits", "description": "Similate a game dodge with a split from the top of the box, down the alley into your shot. You can also similate a potential slide with a bounce out, into a redodge.", "reps": "5 each side"},
        {"url": "https://www.youtube.com/embed/o1SBiX23JYo?start=150&end=160", "title": "Up the Hash Shooting", "description": "Can be done with or without a feeder. Start around gle, and with yoru stick outstretched towards the sideline, run up the hash and shoot as you run upfeild", "reps": "10 each side" },
        {"url": "https://www.youtube.com/embed/ocHH2x9xlUI?start=236&end=242", "title": "Split to Hitch", "description": "Starting at X, split dodge upfield and make your way a few yards past GLE. Then bounce out as if you are going to pass, and hitch. Step a few more feet upfield and take a step down shot.", "reps": "8 each side"},
        {"url": "https://www.youtube.com/embed/nJeWuDnikww?start=277&end=284", "title": "Front and Center Step Downs", "description": "Go 10-12 yards away from the goal straight in front, and take a step down shot. Pick one corner and try to aim all your shots in that vicinity.", "reps": "10 each side"},
        {"url": "https://www.youtube.com/embed/TDqpPM_dx88?start=245&end=255", "title": "finishers", "description": "Start a few feet in front of the net. Toss up a ball, make at least 2 fakes, and finish in a corner. Try to vary your fakes and which corner you shoot into.", "reps": "8 each side"},
        {"url": "https://www.youtube.com/embed/TDqpPM_dx88?start=146&end=152", "title": "Step Down and Hitch", "description": "From the top of the alley, load into a step down shot. Then, reset, and load into the same shot. This time, however, hitch and take an on the run shot down the alley.", "reps": "5 each side"},
        {"url": "https://www.youtube.com/embed/TDqpPM_dx88?start=389&end=406", "title": "5 Shot Combo", "description": "From the top of the alley, load into a step down shot. Then, reset, and load a step down with the other hand. For the third shot keep the hand with the inside hand, then split to the outside to take an on the run shot. Then repeat this split exept start with your outside hand. For the last shot take an inside finish around the crease. You don't need a feeder; instead just pick up a ground ball in your inside shot.", "reps": "4 each side"}]

        wall=request.form.get("wall")
        net=request.form.get("net")
        time=request.form.get("time")
        balls=request.form.get("balls")
        
        choose=[]
        workout=[]
        warm_up1 = []
        taken_numbers=[]
        warm_up=[]
        random_list=[]

        numbers=2
        
        total_numbers=0
        total_numbers2=0
        real_numbers=0

        
        if (net=="net"):
            net_true=True
            for i in warm_shooting:
                choose.append(i)
                warm_up.append(i)
                total_numbers+=1
        
        if (wall=="wall"):
            wall_true=True
            for i in wall_ball:
                choose.append(i)
                warm_up.append(i)
                total_numbers+=1

        if (net=="net"):
            for i in little_ball:
                choose.append(i)
            if balls=="10-20" or balls=="20+":
                for i in shooting:
                    choose.append(i)
                    total_numbers+=1
        for i in no_ball:
            choose.append(i)
            total_numbers+=1
        
        
        if (time=="30min"):
            numbers=numbers*3
        if (time=="60min"):
            numbers=numbers*5
        if (time=="90min"):
            numbers=numbers*7
        if(time=="120min"):
            numbers=numbers*10
    
        if net=="net" or wall=="wall":
            warm_up1.append(random.sample(choose[:len(warm_up)], 3))
            taken_numbers.append(warm_up1)
        else:
            warm_up1.append(random.sample(choose[:len(no_ball)], 3))
            taken_numbers.append(warm_up1)




        workout.append(random.sample(choose, numbers))
        for i in range(len(workout[0])):
            while workout[0][i] in taken_numbers[0][0]:
                workout[0][i]=random.sample(choose,1)[0]
                
            
            
        return render_template("calculated2.html", random_list=random_list, real_numbers=real_numbers, taken_numbers=taken_numbers, numbers=numbers, workout=workout, warm_up1=warm_up1, choose=choose)
    if (request.method == 'GET'):
        return render_template("calc.html", x="hello")
    