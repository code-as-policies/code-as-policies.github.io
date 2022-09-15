$(document).ready(function() {
    // bibtex
    var editor = CodeMirror.fromTextArea(document.getElementById("bibtex"), {
        lineNumbers: false,
        lineWrapping: true,
        readOnly:true
    });

    var current_cmd_idxs = {
        "blocks": 1,
        "blocksbowls": 1,
        "fbp": 1,
        "draw": 1,
        "mobilenav": 1,
        "mobilemnp": 1
    }

    function setTime(vid, time) {
        vid.play();
        vid.pause();
        vid.currentTime = time;
        vid.play();
    }

    var vid_start_times = {
        "blocks": {
            1: 0 * 60 + 3,
            2: 1 * 60 + 34,
            3: 2 * 60 + 18,
            4: 2 * 60 + 51,
            5: 3 * 60 + 4,
            6: 4 * 60 + 52,
            7: 6* 60 + 12,
            8: 7 * 60 + 32,
            9: 8 * 60 + 55,
            10: 9 * 60 + 7,
            11: 9 * 60 + 43,
            12: 11 * 60 + 18
        },
        "blocksbowls": {
            1: 0 * 60 + 3,
            2: 0 * 60 + 50,
            3: 1 * 60 + 27,
            4: 1 * 60 + 50,
            5: 2 * 60 + 58,
            6: 4 * 60 + 17,
            7: 4 * 60 + 30,
            8: 4 * 60 + 42,
            9: 5 * 60 + 43
        },
        "fbp": {
            1: 0 * 60 + 2,
            2: 0 * 60 + 24,
            3: 0 * 60 + 47,
            4: 1 * 60 + 33,
            5: 3 * 60 + 32,
            6: 4 * 60 + 11,
            7: 4 * 60 + 57,
        },
        "draw": {
            1: 0 * 60 + 3,
            2: 0 * 60 + 40,
            3: 1 * 60 + 4,
            4: 2 * 60 + 23,
            5: 3 * 60 + 6,
            6: 3 * 60 + 44,
            7: 4 * 60 + 16,
            8: 5 * 60 + 0,
            9: 5 * 60 + 32,
            10: 6 * 60 + 37,
            11: 7 * 60 + 53,
        }
    }

    var vid_end_times = {
        "blocks": {
            1: 1 * 60 + 32,
            2: 2 * 60 + 17,
            3: 2 * 60 + 50,
            4: 3 * 60 + 3,
            5: 4 * 60 + 51,
            6: 6 * 60 + 10,
            7: 7 * 60 + 29,
            8: 8 * 60 + 53,
            9: 9 * 60 + 5,
            10: 9 * 60 + 41,
            11: 11 * 60 + 15,
            12: 12 * 60 + 47
        },
        "blocksbowls": {
            1: 0 * 60 + 48,
            2: 1 * 60 + 25,
            3: 1 * 60 + 49,
            4: 2 * 60 + 57,
            5: 4 * 60 + 16,
            6: 4 * 60 + 29,
            7: 4 * 60 + 41,
            8: 5 * 60 + 42,
            9: 6 * 60 + 11
        },
        "fbp": {
            1: 0 * 60 + 22,
            2: 0 * 60 + 43,
            3: 1 * 60 + 32,
            4: 3 * 60 + 27,
            5: 4 * 60 + 10,
            6: 4 * 60 + 53,
            7: 5 * 60 + 32,
        },
        "draw": {
            1: 0 * 60 + 38,
            2: 1 * 60 + 3,
            3: 2 * 60 + 22,
            4: 3 * 60 + 5,
            5: 3 * 60 + 43,
            6: 4 * 60 + 15,
            7: 4 * 60 + 59,
            8: 5 * 60 + 31,
            9: 6 * 60 + 21,
            10: 7 * 60 + 52,
            11: 8 * 60 + 33,
        }
    }

    var vid_should_check_pause = {
        'blocks': false,
        'blocksbowls': false,
        'fbp': false,
        'draw': false
    };

    Object.keys(vid_should_check_pause).forEach(domain_name => {
        const events = ["seeking", "ended"];
        events.forEach(event => {
            $("#vid_" + domain_name)[0].addEventListener(event, function() {
                vid_should_check_pause[domain_name] = false;
            });
        })
    });

    // demos
    $('select').on('change', function() {
        var sep_idx = this.value.indexOf('_');
        var domain_name = this.value.substring(0, sep_idx);
        var desired_cmd_idx = parseInt(this.value.substring(sep_idx + 1));

        var current_cmd_idx = current_cmd_idxs[domain_name];
        if (current_cmd_idx != desired_cmd_idx) {
            // hide current content
            var current_content = $('#content_' + domain_name + "_" + current_cmd_idx.toString());
            current_content.hide();

            // stop current videos
            if (domain_name.startsWith("mobile")) {
                $('#vid_1_' + domain_name + "_" + current_cmd_idx.toString()).get(0).pause();
                // $('#vid_2_' + domain_name + "_" + current_cmd_idx.toString()).get(0).pause();
            } else {
                // set vid timestamp
                var vid = $("#vid_" + domain_name)[0];
                var time = vid_start_times[domain_name][desired_cmd_idx];
                setTime(vid, time);

                // pause video after current segment finishes 
                vid_should_check_pause[domain_name] = true;
                var pausing_function = function() {
                    if (vid_should_check_pause[domain_name]) {
                        if (this.currentTime >= vid_end_times[domain_name][desired_cmd_idx]) {
                            this.pause();
                            this.removeEventListener("timeupdate", pausing_function);
                        }
                    } else {
                        this.removeEventListener("timeupdate", pausing_function);
                    }
                };
                vid.addEventListener("timeupdate", pausing_function);
            }

            // show desired content
            var desired_content = $('#content_' + domain_name + "_" + desired_cmd_idx.toString());
            desired_content.show();

            // set current to desired
            current_cmd_idxs[domain_name] = desired_cmd_idx;
        }
    });
});