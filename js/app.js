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

    // demos
    $('select').on('change', function() {
        var sep_idx = this.value.indexOf('_');
        var domain_name = this.value.substring(0, sep_idx);
        var desired_cmd_idx = parseInt(this.value.substring(sep_idx + 1));
        console.log(domain_name);
        console.log(desired_cmd_idx);

        var current_cmd_idx = current_cmd_idxs[domain_name];
        if (current_cmd_idx != desired_cmd_idx) {
            // hide current content
            var current_content = $('#content_' + domain_name + "_" + current_cmd_idx.toString());
            current_content.hide();

            // stop current videos
            if (domain_name.startsWith("mobile")) {
                $('#vid_1_' + domain_name + "_" + current_cmd_idx.toString()).get(0).pause();
                // $('#vid_2_' + domain_name + "_" + current_cmd_idx.toString()).get(0).pause();
            }

            // show desired content
            var desired_content = $('#content_' + domain_name + "_" + desired_cmd_idx.toString());
            desired_content.show();

            // set current to desired
            current_cmd_idxs[domain_name] = desired_cmd_idx;

            // set vido timestamp
        }
    });
    



// var frameNumber = 0, // start video at frame 0
//     // lower numbers = faster playback
//     playbackConst = 500, 
//     // get page height from video duration
//     setHeight = document.getElementById("main"), 
//     // select video element         
//     vid = document.getElementById('v0'); 
//     // var vid = $('#v0')[0]; // jquery option

    
// // Use requestAnimationFrame for smooth playback
// function scrollPlay(){  
//   var frameNumber  = window.pageYOffset/playbackConst;
//   vid.currentTime  = frameNumber;
//   window.requestAnimationFrame(scrollPlay);
// console.log('scroll');
// }
    
// // dynamically set the page height according to video length
// vid.addEventListener('loadedmetadata', function() {
//   setHeight.style.height = Math.floor(vid.duration) * playbackConst + "px";
// });

    
//     window.requestAnimationFrame(scrollPlay);
});