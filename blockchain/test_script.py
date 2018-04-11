# --------------------------------------- START OF LICENSE NOTICE ------------------------------------------------------
# Copyright (c) 2018 Soroco Private Limited. All rights reserved.
#
# NO WARRANTY. THE PRODUCT IS PROVIDED BY SOROCO "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
# SHALL SOROCO BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THE PRODUCT, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
# DAMAGE.
# ---------------------------------------- END OF LICENSE NOTICE -------------------------------------------------------
#
#   Primary Author: Shivam Vijaywargiya <shivam.vijaywargiya@soroco.com>
#
#   Purpose: A short description of the purpose of this source file ...
import uuid

from argon2 import PasswordHasher

password = '198922113'
username = 'vijaywargiya'
ph = PasswordHasher()
key = ph.hash(password + username)
print(key)
key = ph.hash(password + username)
print(key)
key = ph.hash(password + username)
print(key)
key = ph.hash(username + username)
print(key)
