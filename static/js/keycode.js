(function() {
/**
 * A modified version of the keycode plugin by Jonathan Tang,
 * specialized for keycodes used by AoE2
 * http://jonathan.tang.name/code/js_keycode
 */

var modifiers = ['Ctrl', 'Alt', 'Shift'];

//Derived from http://msdn.microsoft.com/en-us/library/windows/desktop/dd375731(v=vs.85).aspx
var key_names = {
    //AoK uses 251-255 for mouse key codes
	// 1 : 'Lbutton', // Left mouse button
	// 2 : 'Rbutton', // Right mouse button
	// 3 : 'Cancel', // Control-break processing
	// 4 : 'Mbutton', // Middle mouse button (three-button mouse)
	// 5 : 'Xbutton1', // X1 mouse button
	// 6 : 'Xbutton2', // X2 mouse button
//'-'  : 0x07, // Undefined
	8 : 'Backspace', // BACKSPACE key
	9 : 'Tab', // TAB key
//'-'  : 0x0A-0B, // Reserved
	12 : 'Clear', // CLEAR key
	13 : 'Enter', // ENTER key
//'-'  : 0x0E-0F, // Undefined
	16 : 'Shift', // SHIFT key
	17 : 'Ctrl', // CTRL key
	18 : 'Alt', // ALT key
	19 : 'Pause', // PAUSE key
	20 : 'Caps Lock', // CAPS LOCK key
	21 : 'Kana', // IME Kana mode
	21 : 'Hanguel', // IME Hanguel mode (maintained for compatibility; use <strong>VK_HANGUL</strong>)
	21 : 'Hangul', // IME Hangul mode
//'-'  : 0x16, // Undefined
	23 : 'Junja', // IME Junja mode
	24 : 'Final', // IME final mode
	25 : 'Hanja', // IME Hanja mode
	25 : 'Kanji', // IME Kanji mode
//'-'  : 0x1A, // Undefined
	27 : 'Escape', // ESC key
	28 : 'Convert', // IME convert
	29 : 'Nonconvert', // IME nonconvert
	30 : 'Accept', // IME accept
	31 : 'Mode Change', // IME mode change request
	32 : 'Space', // SPACEBAR
	33 : 'Page Up', // PAGE UP key
	34 : 'Page Down', // PAGE DOWN key
	35 : 'End', // END key
	36 : 'Home', // HOME key
	37 : 'Left', // LEFT ARROW key
	38 : 'Up', // UP ARROW key
	39 : 'Right', // RIGHT ARROW key
	40 : 'Down', // DOWN ARROW key
	41 : 'Select', // SELECT key
	42 : 'Print', // PRINT key
	43 : 'Execute', // EXECUTE key
	44 : 'Print Screen', // PRINT SCREEN key
	45 : 'Insert', // INS key
	46 : 'Delete', // DEL key
	47 : 'Help', // HELP key
//''  : 0x30, // 0 key
//''  : 0x31, // 1 key
//''  : 0x32, // 2 key
//''  : 0x33, // 3 key
//''  : 0x34, // 4 key
//''  : 0x35, // 5 key
//''  : 0x36, // 6 key
//''  : 0x37, // 7 key
//''  : 0x38, // 8 key
//''  : 0x39, // 9 key
//'-'  : 0x3A-40, // Undefined
//''  : 0x41, // A key
//''  : 0x42, // B key
//''  : 0x43, // C key
//''  : 0x44, // D key
//''  : 0x45, // E key
//''  : 0x46, // F key
//''  : 0x47, // G key
//''  : 0x48, // H key
//''  : 0x49, // I key
//''  : 0x4A, // J key
//''  : 0x4B, // K key
//''  : 0x4C, // L key
//''  : 0x4D, // M key
//''  : 0x4E, // N key
//''  : 0x4F, // O key
//''  : 0x50, // P key
//''  : 0x51, // Q key
//''  : 0x52, // R key
//''  : 0x53, // S key
//''  : 0x54, // T key
//''  : 0x55, // U key
//''  : 0x56, // V key
//''  : 0x57, // W key
//''  : 0x58, // X key
//''  : 0x59, // Y key
//''  : 0x5A, // Z key
	91 : 'Left Win', // Left Windows key (Natural keyboard) 
	92 : 'Right Win', // Right Windows key (Natural keyboard)
	93 : 'Menu', // Applications key (Natural keyboard)
//'-'  : 0x5E, // Reserved
	95 : 'Sleep', // Computer Sleep key
	96 : 'Num0', // Numeric keypad 0 key
	97 : 'Num1', // Numeric keypad 1 key
	98 : 'Num2', // Numeric keypad 2 key
	99 : 'Num3', // Numeric keypad 3 key
	100 : 'Num4', // Numeric keypad 4 key
	101 : 'Num5', // Numeric keypad 5 key
	102 : 'Num6', // Numeric keypad 6 key
	103 : 'Num7', // Numeric keypad 7 key
	104 : 'Num8', // Numeric keypad 8 key
	105 : 'Num9', // Numeric keypad 9 key
	106 : 'Num*', // Multiply key
	107 : 'Num+', // Add key
	108 : 'Num,', // Separator key
	109 : 'Num-', // Subtract key
	110 : 'Num.', // Decimal key
	111 : 'Num/', // Divide key
	112 : 'F1', // F1 key
	113 : 'F2', // F2 key
	114 : 'F3', // F3 key
	115 : 'F4', // F4 key
	116 : 'F5', // F5 key
	117 : 'F6', // F6 key
	118 : 'F7', // F7 key
	119 : 'F8', // F8 key
	120 : 'F9', // F9 key
	121 : 'F10', // F10 key
	122 : 'F11', // F11 key
	123 : 'F12', // F12 key
	124 : 'F13', // F13 key
	125 : 'F14', // F14 key
	126 : 'F15', // F15 key
	127 : 'F16', // F16 key
	128 : 'F17', // F17 key
	129 : 'F18', // F18 key
	130 : 'F19', // F19 key
	131 : 'F20', // F20 key
	132 : 'F21', // F21 key
	133 : 'F22', // F22 key
	134 : 'F23', // F23 key
	135 : 'F24', // F24 key
//'-'  : 0x88-8F, // Unassigned
	144 : 'Num Lock', // NUM LOCK key
	145 : 'Scroll Lock', // SCROLL LOCK key
//''  : 0x92-96, // OEM specific
//'-'  : 0x97-9F, // Unassigned
	160 : 'Lshift', // Left SHIFT key
	161 : 'Rshift', // Right SHIFT key
	162 : 'Lcontrol', // Left CONTROL key
	163 : 'Rcontrol', // Right CONTROL key
	164 : 'Left Menu', // Left MENU key
	165 : 'Right Menu', // Right MENU key
	166 : 'Browser Back', // Browser Back key
	167 : 'Browser Forward', // Browser Forward key
	168 : 'Browser Refresh', // Browser Refresh key
	169 : 'Browser Stop', // Browser Stop key
	170 : 'Browser Search', // Browser Search key 
	171 : 'Browser Favorites', // Browser Favorites key
	172 : 'Browser Home', // Browser Start and Home key
	173 : 'Volume Mute', // Volume Mute key
	174 : 'Volume Down', // Volume Down key
	175 : 'Volume Up', // Volume Up key
	176 : 'Media Next Track', // Next Track key
	177 : 'Media Prev Track', // Previous Track key
	178 : 'Media Stop', // Stop Media key
	179 : 'Media Play Pause', // Play/Pause Media key
	180 : 'Launch Mail', // Start Mail key
	181 : 'Launch Select Media', // Select Media key
	182 : 'Launch App1', // Start Application 1 key
	183 : 'Launch App2', // Start Application 2 key
//'-'  : 0xB8-B9, // Reserved
	186 : ';', // Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the ';:' key
	187 : '=', // For any country/region, the '+' key
	188 : ',', // For any country/region, the ',' key
	189 : '-', // For any country/region, the '-' key
	190 : '.', // For any country/region, the '.' key
	191 : '/', // Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the '/?' key
	192 : '`', // Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the '`~' key
//'-'  : 0xC1-D7, // Reserved
//'-'  : 0xD8-DA, // Unassigned
	219 : '[', // Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the '[{' key
	220 : '\\', // Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the '\|' key
	221 : ']', // Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the ']}' key
	222 : '\'', // Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the 'single-quote/double-quote' key
	223 : 'Misc', // Used for miscellaneous characters; it can vary by keyboard.
//'-'  : 0xE0, // Reserved
//''  : 0xE1, // OEM specific
	226 : 'Angle Bracket', // Either the angle bracket key or the backslash key on the RT 102-key keyboard
//''  : 0xE3-E4, // OEM specific
	229 : 'IME Process', // IME PROCESS key
//''  : 0xE6, // OEM specific
	231 : 'Packet', //  Used to pass Unicode characters as if they were keystrokes.
//'-'  : 0xE8, // Unassigned
//''  : 0xE9-F5, // OEM specific
	246 : 'Attn', // Attn key
	247 : 'CrSel', // CrSel key
	248 : 'ExSel', // ExSel key
	249 : 'Erase EOF', // Erase EOF key
	250 : 'Play', // Play key
	// 251 : 'Zoom', // Zoom key
	// 252 : 'Noname', // Reserved 
	// 253 : 'Pa1', // PA1 key
	// 254 : 'Oem Clear' // Clear key
    //These keys are remapped to AoK codes for various mouse buttons
	251 : 'Extra Button 2', // AoK uses this for Extra Button 2
	252 : 'Extra Button 1', // AoK uses this for Extra Button 1
	253 : 'Middle Button', // AoK uses this for Middle Button
	254 : 'Wheel Up', // AoK uses this for Wheel Up
	255 : 'Wheel Down' // AoK uses this for Wheel Down
}


function capitalize(str) { 
    return str.substr(0,1).toUpperCase() + str.substr(1).toLowerCase(); 
};

var is_gecko = navigator.userAgent.indexOf('Gecko') != -1,
    is_ie = navigator.userAgent.indexOf('MSIE') != -1,
    is_windows = navigator.platform.indexOf('Win') != -1,
    is_opera = window.opera && window.opera.version() < '9.5',
    is_konqueror = navigator.vendor && navigator.vendor.indexOf('KDE') != -1,
    is_icab = navigator.vendor && navigator.vendor.indexOf('iCab') != -1;

var GECKO_IE_KEYMAP = {
    59: 186, // ;: in Mozilla
    173: 189, // -_ in Mozilla
    61: 187, // =+ in Mozilla
    2: 253 //middle button
};

//the original library used ascii codes for some symbols.
//This would affect the keymaps for Opera, Konqueror et al
//I haven't found this worth the time to fix considering their market share
//and the intended audience of this website.
//Hence, all this code is inoperative
// var OPERA_KEYMAP = {};

// Browser detection taken from quirksmode.org
// if(is_opera && is_windows) {
    // KEY_MAP = OPERA_KEYMAP;
// } else if(is_opera || is_konqueror || is_icab) {
    // var unshift = [33, 64, 35, 36, 37, 94, 38, 42, 40, 41, 
                   // 58, 43, 60, 95, 62, 63, 124, 34];
    // KEY_MAP = OPERA_KEYMAP;
    // for(var i = 0; i < unshift.length; ++i) {
        // KEY_MAP[unshift[i]] = shifted_symbols[unshift[i]];
    // }
// } else {
    // IE and Gecko are close enough that we can use the same map for both,
    // and the rest of the world (eg. Opera 9.50) seems to be standardizing
    // on them
KEY_MAP = GECKO_IE_KEYMAP;
// }

// if(is_konqueror) {
    // KEY_MAP[0] = 45;
    // KEY_MAP[127] = 46;
    // KEY_MAP[45] = 95;
// }
//remap middle button to 253
KEY_MAP[2] = 253;

// function fn_name(code) {
    // if(code >= 112 && code <= 123) return 'F' + (code - 111);
    // return false;
// };
// function num_name(code) {
    // if(code >= 96 && code < 106) return 'Num' + (code - 96);
    // switch(code) {
        // case 106: return 'Num*';
        // case 111: return 'Num/';
        // case 110: return 'Num.';
        // default: return false;
    // }
// };

// var current_keys = {
    // codes: {},
    // ctrl: false,
    // alt: false,
    // shift: false
// };

// function update_current_modifiers(key) {
    // current_keys.ctrl = key.ctrl;
    // current_keys.alt = key.alt;
    // current_keys.shift = key.shift;
// };

function same_modifiers(key1, key2) {
    return key1.ctrl === key2.ctrl
        && key1.alt === key2.alt
        && key1.shift === key2.shift;
};

if(typeof window.KeyCode != "undefined") {
    var _KeyCode = window.KeyCode;
}

var KeyCode = window.KeyCode = {
    no_conflict: function() {
        window.KeyCode = _KeyCode;
        return KeyCode;
    },

    /** Generates a function key code from a number between 1 and 12 */
    // fkey: function(num) { return 111 + num; },

    /** 
     * Generates a numeric keypad code from a number between 0 and 9. 
     * Also works for (some) arithmetic operators.  The mappings are:
     *
     * *: 106, /: 111, .: 110
     *
     * + and - are not supported because the keycodes generated by Mozilla
     * conflict with the non-keypad codes.  The same applies to all the
     * arithmetic keypad keys on Konqueror and early Opera.
     */
    // numkey: function(num) { 
        // switch(num) {
            // case '*': return 106;
            // case '/': return 111;
            // case '.': return 110;
            // default: return 96 + num;
        // }
    // },

    /** Checks if two key objects are equal. */
    key_equals: function(key1, key2) {
        return key1.code == key2.code && same_modifiers(key1, key2);
    },

    /** Translates a keycode to its normalized value. */
    translate_key_code: function(code) {
        return KEY_MAP[code] || code;
    },

    /** Translates a keyDown event to a normalized key event object.  The
     * object has the following fields:
     * { int code; boolean shift, boolean alt, boolean ctrl }
     */
    translate_event: function(e) {
        e = e || window.event;
        var code = e.which || e.keyCode;
        return {
            code: KeyCode.translate_key_code(code),
            shift: e.shiftKey,
            alt: e.altKey,
            ctrl: e.ctrlKey
        };
    },

    /**
     * Keydown event listener to update internal state of which keys are
     * currently pressed.
     */ 
    // key_down: function(e) {
        // var key = KeyCode.translate_event(e);
        // current_keys.codes[key.code] = key.code;
        // update_current_modifiers(key);
    // },

    // /**
     // * Keyup event listener to update internal state.
     // */
    // key_up: function(e) {
        // var key = KeyCode.translate_event(e);
        // delete current_keys.codes[key.code];
        // update_current_modifiers(key);
    // },

    // /**
     // * Returns true if the key spec (as returned by translate_event) is
     // * currently held down.
     // */
    // is_down: function(key) {
        // var code = key.code;
        // if(code == KeyCode.Ctrl) return current_keys.ctrl;
        // if(code == KeyCode.Alt) return current_keys.alt;
        // if(code == KeyCode.Shift) return current_keys.shift;

        // return current_keys.codes[code] !== undefined
            // && same_modifiers(key, current_keys);
    // },

    /** Returns a string representation of a key event suitable for the
     * shortcut.js or JQuery HotKeys plugins.  Also makes a decent UI display.
     */
    hot_key: function(key) {
        var pieces = [];
        for(var i = 0; i < modifiers.length; ++i) {
            var modifier = modifiers[i];
            if(key[modifier.toLowerCase()] && modifier != key_names[key.code]) {
                pieces.push(capitalize(modifier));
            }
        }

        var c = key.code;
        var key_name = key_names[c] || 
            // fn_name(c) || num_name(c) ||
            String.fromCharCode(c);
        pieces.push(key_name)
        return pieces.join('+');
    }
};

// Add key constants 
for(var code in key_names) {
    KeyCode[key_names[code]] = code;
}
})();
