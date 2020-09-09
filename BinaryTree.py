# Tree Node with different things that helps to build the Tree and print it
class TreeNode():
    # It instantiates the class
    def __init__ (self, val):
        self.val = val
        self.place = 0
        self.left = None
        self.right = None

# It returns the head of the Tree that was build with the plane Tree "s"
def getTree(s):
    if type(s) == str:
        if ',' in s:
            key = ','
            s.replace(' ','')
        else:
            key = ' ' 
        aux = s.split(key)
        key = 'null' if 'null' in aux else ('None' if 'None' in aux else '-1')
        mylist = [None if x == key else int(x) for x in aux]
    elif type(s) == list and 0 < len(s) and type(s[0]) == int:
        mylist = s if None in s else [None if x == -1 else int(x) for x in s]
    else:
        print('Wrong format for the input')
        return None
    # Stars building the tree
    head = TreeNode(mylist[0])
    queue = [head]
    i = 1
    while queue:
        aux = []
        for q in queue:
            if mylist[i] != None:
                q.left = TreeNode(mylist[i])
                aux.append(q.left)
            i += 1
            if mylist[i] != None:
                q.right = TreeNode(mylist[i])
                aux.append(q.right)
            i += 1
        queue = aux
    return head

# It returns the full draw of the tree in 2dimensions O(N)
def getStr(head):
    if head == None:
        return 'No elements in the Tree'
    # Gets the in-order list of the values and its place
    listInOrder, stack = [], []
    node = head
    count = 0
    while(stack or node):
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            listInOrder.append(node.val)
            node.place = count
            count += 1
            node = node.right
    # Gets the sizes of each node
    sizes, sumsizes = [], []
    for x in listInOrder:
        sizes.append(len(str(x)))
    past = 1
    for x in sizes:
        sumsizes.append(past)
        past += x
    sumsizes.append(past)
    # Builds the output string
    outstr = '\n'
    queue = [head]
    while queue:
        aux = []
        past, nextpast = 0, 0
        line, nextline = '', ''
        for q in queue:
            if q.left and q.right:
                aux.append(q.left)
                aux.append(q.right)
                # Print of the _ and the values of the nodes
                line += ' '*(sumsizes[q.left.place+1]-past) + '_'*(sumsizes[q.place]-sumsizes[q.left.place+1]) + str(q.val) + '_'*(sumsizes[q.right.place]-sumsizes[q.place+1])
                past = sumsizes[q.right.place]
                # Print of the arms of the Tree
                nextline += ' '*(sumsizes[q.left.place+1]-nextpast-1) + '/' + ' '*(sumsizes[q.right.place]-sumsizes[q.left.place+1]) + '\\' + ' '*(sizes[q.right.place]-1)
                nextpast = sumsizes[q.right.place+1]
            elif q.left:
                aux.append(q.left)
                # Print of the _ and the values of the nodes
                line += ' '*(sumsizes[q.left.place+1]-past) + '_'*(sumsizes[q.place]-sumsizes[q.left.place+1]) + str(q.val)
                past = sumsizes[q.place+1]
                # Print of the arms of the Tree
                nextline += ' '*(sumsizes[q.left.place+1]-nextpast-1) + '/'
                nextpast = sumsizes[q.left.place+1]
            elif q.right:
                aux.append(q.right)
                # Print of the _ and the values of the nodes
                line += ' '*(sumsizes[q.place]-past)+str(q.val)+'_'*(sumsizes[q.right.place]-sumsizes[q.place+1])
                past = sumsizes[q.right.place]
                # Print of the arms of the Tree
                nextline += ' '*(sumsizes[q.right.place]-nextpast) + '\\' + ' '*(sizes[q.right.place]-1)
                nextpast = sumsizes[q.right.place+1]
            else:
                line += ' '*(sumsizes[q.place]-past)+str(q.val)
                past = sumsizes[q.place+1]
        # Add the lines to the output string
        outstr += line + '\n' + nextline + '\n'
        queue = aux
    return outstr[:-1]

# it Returns the Tree in its plane form
def getList(Node):
    treeList = []
    stack = [Node]
    while stack:
        q = stack.pop()
        if q:
            treeList.append(q.val)
            stack.append(q.right)
            stack.append(q.left)
        else:
            treeList.append(None)
    return treeList

##################################################
# Example code
##################################################
#s = '863 64 217 343 207 391 145 304 248 80 389 225 86 168 233 56 349 114 223 284 269 57 71 334 149 4 411 399 279 87 352 52 -1 -1 105 78 427 181 250 297 344 221 51 166 111 378 374 266 -1 296 28 59 424 44 193 160 229 318 -1 242 406 -1 328 175 199 48 342 408 -1 368 -1 116 25 -1 47 338 215 50 231 -1 262 189 -1 153 -1 340 -1 277 -1 -1 -1 41 -1 -1 197 10 224 326 120 108 414 228 316 310 117 109 367 91 119 8 -1 -1 -1 -1 382 -1 -1 -1 361 332 -1 -1 118 425 -1 205 -1 -1 423 150 134 -1 182 131 327 -1 337 325 386 173 196 291 -1 365 32 247 -1 -1 -1 -1 -1 -1 130 419 187 219 -1 -1 180 177 66 420 285 161 37 76 303 154 377 -1 353 -1 366 370 309 -1 170 272 -1 -1 -1 -1 333 431 -1 317 -1 -1 206 292 -1 192 -1 -1 -1 -1 -1 39 -1 -1 -1 -1 -1 -1 396 357 259 300 -1 240 -1 -1 265 -1 330 335 195 256 -1 428 -1 -1 -1 -1 -1 -1 -1 -1 77 -1 410 204 -1 -1 99 360 320 62 324 -1 163 415 -1 -1 214 141 421 -1 90 -1 283 143 354 17 110 218 19 75 -1 351 36 167 191 244 429 174 404 123 74 294 165 -1 79 275 67 -1 381 243 267 -1 -1 -1 -1 394 413 -1 -1 230 -1 213 176 22 -1 -1 -1 83 -1 -1 -1 -1 409 -1 358 -1 398 7 157 -1 255 -1 -1 -1 373 323 -1 346 282 234 222 26 54 270 49 -1 -1 200 -1 302 -1 -1 -1 138 -1 290 -1 -1 -1 -1 339 314 216 124 -1 171 274 13 308 -1 376 315 70 403 355 137 388 142 383 31 -1 260 92 58 30 281 159 209 251 407 -1 23 144 43 -1 94 132 -1 -1 295 -1 -1 241 306 245 -1 -1 179 -1 -1 -1 98 -1 249 -1 -1 -1 -1 -1 136 -1 -1 -1 -1 -1 -1 106 -1 307 -1 -1 -1 -1 -1 -1 -1 169 -1 -1 -1 372 -1 -1 -1 299 -1 112 -1 287 115 -1 -1 -1 -1 -1 -1 53 -1 16 -1 -1 -1 125 278 253 401 -1 18 384 201 183 188 400 20 276 402 122 -1 -1 198 -1 -1 203 254 -1 63 -1 208 -1 258 178 -1 129 246 34 393 235 220 -1 -1 151 -1 185 100 -1 286 -1 416 88 190 -1 -1 -1 -1 369 103 341 -1 1 162 82 133 -1 -1 35 -1 9 -1 -1 -1 11 107 29 -1 -1 -1 -1 68 -1 412 -1 405 128 -1 -1 -1 -1 -1 -1 -1 417 -1 311 418 -1 -1 -1 -1 -1 12 -1 -1 322 226 93 263 359 38 126 73 -1 312 -1 -1 -1 -1 2 -1 -1 329 127 211 -1 60 -1 -1 172 -1 -1 -1 -1 -1 -1 5 -1 -1 140 -1 395 -1 -1 -1 84 15 -1 -1 -1 155 -1 257 264 -1 -1 148 95 -1 -1 -1 14 380 350 -1 -1 -1 -1 375 -1 -1 371 -1 -1 65 89 298 -1 -1 236 -1 -1 184 102 158 72 -1 -1 -1 -1 -1 305 -1 -1 46 293 -1 101 -1 -1 -1 -1 362 -1 -1 -1 104 -1 -1 -1 -1 -1 348 -1 186 -1 -1 -1 -1 321 113 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 390 364 -1 268 -1 -1 -1 331 -1 -1 -1 -1 -1 -1 319 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 69 239 -1 -1 152 135 -1 -1 -1 -1 55 -1 -1 202 261 96 -1 -1 -1 -1 6 -1 301 -1 -1 -1 -1 -1 -1 363 -1 -1 -1 -1 -1 -1 -1 -1 -1 238 252 97 -1 -1 -1 -1 392 -1 -1 -1 288 -1 -1 -1 271 -1 -1 -1 -1 -1 422 -1 -1 -1 212 -1 387 24 3 -1 -1 -1 21 40 -1 -1 -1 -1 273 139 -1 -1 -1 -1 237 61 -1 -1 81 -1 -1 -1 -1 -1 147 347 227 -1 -1 33 -1 385 -1 121 -1 -1 -1 -1 289 -1 397 -1 426 -1 -1 -1 -1 -1 -1 -1 -1 232 -1 280 356 164 -1 -1 45 336 -1 146 -1 -1 -1 -1 -1 -1 379 430 194 -1 -1 313 42 85 210 345 27 -1 -1 -1 -1 -1 156 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1'
s = "47 42 52 41 44 50 64 40 -1 43 45 49 51 63 77 -1 -1 -1 -1 -1 46 48 -1 -1 -1 55 -1 75 88 -1 -1 -1 -1 53 58 69 76 81 94 -1 54 56 60 68 73 -1 -1 79 87 92 100 -1 -1 -1 57 59 61 66 -1 72 74 78 80 85 -1 89 93 96 102 -1 -1 -1 -1 -1 62 65 67 71 -1 -1 -1 -1 -1 -1 -1 84 86 -1 90 -1 -1 95 99 101 -1 -1 -1 -1 -1 -1 -1 70 -1 83 -1 -1 -1 -1 91 -1 -1 98 -1 -1 -1 -1 -1 82 -1 -1 -1 97 -1 -1 -1 -1 -1"
#s = [ 1, 2, 3, None, 4, None, 5, None, None, 6, None, None, None ]
head = getTree(s)
print(getStr(head))
print("The list of the Tree is:",getList(head))