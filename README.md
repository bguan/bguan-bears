# Starlette API Server to Classify Bears

A dockerized Starlette ASGI server that can classify an image as Black, Grizzly or Teddy bear.

Just following the excellent and fun [Lesson 2 of FastAI Course1 v3](https://course.fast.ai/videos/?lesson=2) on exposing a trained image classifier model behind a public API. Also the design and code is shamelessly copied from [Simon Willison's Courgar-or-Not](https://github.com/simonw/cougar-or-not).

A running server is currently deployed to Render.com using FastAI student's credit as of Sep 20th 2019, but no guarantee it will still be running by the time you read this.

## How to Run and Test
 * Clone the project, then run it by:
   * Using Docker 
     * (from parent directory of bguan-bear...)
     * docker build -tbguan-bears bguan-bears
     * docker run -p 8008:8008 bguan-bears
   * or using a Python 3.6+ environment with FastAI and Starlette installed
     * (cd into bguan-bears...)
     * python bears.py serve
 * Point browser at https://localhost:8008 (if running locally) or https://bguan-bears.onrender.com (using my deployed demo server that may be running) and upload photo or submit URL pointing to image
 * You can also programmatically hit the HTTP API directly, e.g. 
   * https://bguan-bears.onrender.com/classify?url=https://n.nordstrommedia.com/id/sr3/8469a1d0-a660-49df-b4e5-96deb40cdbaf.jpeg


Note:
 * To protect server, image upload or submit by URL is limited to 5MB 

