import asyncio
import re
import aiohttp
from urllib.parse import urlparse



import logging
from struct import pack
import re
import base64
from pyrogram.file_id import FileId
from pymongo.errors import DuplicateKeyError
from umongo import Instance, Document, fields
from motor.motor_asyncio import AsyncIOMotorClient
from marshmallow.exceptions import ValidationError
from info import DATABASE_URI, DATABASE_NAME, COLLECTION_NAME, USE_CAPTION_FILTER
from utils import temp 

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


client = AsyncIOMotorClient(DATABASE_URI)
db = client[DATABASE_NAME]
instance = Instance.from_db(db)

@instance.register
class Media(Document):
    file_id = fields.StrField(attribute='_id')
    file_ref = fields.StrField(allow_none=True)
    file_name = fields.StrField(required=True)
    file_size = fields.IntField(required=True)
    file_type = fields.StrField(allow_none=True)
    mime_type = fields.StrField(allow_none=True)
    caption = fields.StrField(allow_none=True)

    class Meta:
        indexes = ('$file_name', )
        collection_name = COLLECTION_NAME


async def save_file(media):
    """Save file in database"""

    # TODO: Find better way to get same file_id for same media to avoid duplicates
    file_id, file_ref = unpack_new_file_id(media.file_id)
    file_name = re.sub(r"(_|\-|\.|\+)", " ", str(media.file_name))
    try:
        file = Media(
            file_id=file_id,
            file_ref=file_ref,
            file_name=file_name,
            file_size=media.file_size,
            file_type=media.file_type,
            mime_type=media.mime_type,
            caption=media.caption.html if media.caption else None,
        )
    except ValidationError:
        logger.exception('Error occurred while saving file in database')
        return False, 2
    else:
        try:
            await file.commit()
        except DuplicateKeyError:      
            logger.warning(
                f'{getattr(media, "file_name", "NO_FILE")} is already saved in database'
            )

            return False, 0
        else:
            logger.info(f'{getattr(media, "file_name", "NO_FILE")} is saved to database')
            return True, 1



async def get_search_results(query, file_type=None, max_results=temp.multi_buttons, offset=0, filter=False):
    """For given query return (results, next_offset)"""

    query = query.strip()
    #if filter:
        #better ?
        #query = query.replace(' ', r'(\s|\.|\+|\-|_)')
        #raw_pattern = r'(\s|_|\-|\.|\+)' + query + r'(\s|_|\-|\.|\+)'
    if not query:
        raw_pattern = '.'
    elif ' ' not in query:
        raw_pattern = r'(\b|[\.\+\-_])' + query + r'(\b|[\.\+\-_])'
    else:
        raw_pattern = query.replace(' ', r'.*[\s\.\+\-_]')
    
    try:
        regex = re.compile(raw_pattern, flags=re.IGNORECASE)
    except:
        return []

    if USE_CAPTION_FILTER:
        filter = {'$or': [{'file_name': regex}, {'caption': regex}]}
    else:
        filter = {'file_name': regex}

    if file_type:
        filter['file_type'] = file_type

    total_results = await Media.count_documents(filter)
    next_offset = offset + max_results

    if next_offset > total_results:
        next_offset = ''

    cursor = Media.find(filter)
    # Sort by recent
    cursor.sort('$natural', -1)
    # Slice files according to offset and max results
    cursor.skip(offset).limit(max_results)
    # Get list of files
    files = await cursor.to_list(length=max_results)

    return files, next_offset, total_results

# query part 1

async def get_filter_results(query, file_type=None, max_resultss=temp.multi_buttons, offsett=0, filter=False):
    """For given query return (results, next_offsett)"""

    query = query.strip()
    #if filter:
        #better ?
        #query = query.replace(' ', r'(\s|\.|\+|\-|_)')
        #raw_pattern = r'(\s|_|\-|\.|\+)' + query + r'(\s|_|\-|\.|\+)'
    if not query:
        raw_pattern = '.'
    elif ' ' not in query:
        raw_pattern = r'(\b|[\.\+\-_])' + query + r'(\b|[\.\+\-_])'
    else:
        raw_pattern = query.replace(' ', r'.*[\s\.\+\-_]')
    
    try:
        regex = re.compile(raw_pattern, flags=re.IGNORECASE)
    except:
        return []

    if USE_CAPTION_FILTER:
        filter = {'$or': [{'file_name': regex}, {'caption': regex}]}
    else:
        filter = {'file_name': regex}

    if file_type:
        filter['file_type'] = file_type

    total_resultss = await Media.count_documents(filter)
    next_offsett = offsett + max_resultss

    if next_offsett > total_resultss:
        next_offsett = ''

    cursor = Media.find(filter)
    # Sort by recent
    cursor.sort('$natural', -1)
    # Slice files according to offsett and max resultss
    cursor.skip(offsett).limit(max_resultss)
    # Get list of files
    files = await cursor.to_list(length=max_resultss)

    return files, next_offsett, total_resultss





# query part 2
async def get_filterr_results(query):
    query = query.strip()
    if not query:
        raw_pattern = '.'
    elif ' ' not in query:
        raw_pattern = r'(\b|[\.\+\-_])' + query + r'(\b|[\.\+\-_])'
    else:
        raw_pattern = query.replace(' ', r'.*[\s\.\+\-_]')
    try:
        regex = re.compile(raw_pattern, flags=re.IGNORECASE)
    except:
        return []
    filter = {'file_name': regex}
    total_results = await Media.count_documents(filter)
    cursor = Media.find(filter)
    cursor.sort('$natural', -1)
    files = await cursor.to_list(length=int(total_results))
    return files

async def get_file_details(query):
    filter = {'file_id': query}
    cursor = Media.find(filter)
    filedetails = await cursor.to_list(length=1)
    return filedetails




async def get_file_details(query):
    filter = {'file_id': query}
    cursor = Media.find(filter)
    filedetails = await cursor.to_list(length=1)
    return filedetails


def encode_file_id(s: bytes) -> str:
    r = b""
    n = 0

    for i in s + bytes([22]) + bytes([4]):
        if i == 0:
            n += 1
        else:
            if n:
                r += b"\x00" + bytes([n])
                n = 0

            r += bytes([i])

    return base64.urlsafe_b64encode(r).decode().rstrip("=")


def encode_file_ref(file_ref: bytes) -> str:
    return base64.urlsafe_b64encode(file_ref).decode().rstrip("=")


def unpack_new_file_id(new_file_id):
    """Return file_id, file_ref"""
    decoded = FileId.decode(new_file_id)
    file_id = encode_file_id(
        pack(
            "<iiqq",
            int(decoded.file_type),
            decoded.dc_id,
            decoded.media_id,
            decoded.access_hash
        )
    )
    file_ref = encode_file_ref(decoded.file_reference)
    return file_id, file_ref


#shortzy 



class Shortzyy:
    """
    A Unofficial Wrapper for Adlinkfly Site and Alternative Sites
    
    :param api_key: Your API key
    :type api_key: str
    :param base_site: The site you want to use, defaults to droplink.co
    :type base_site: str (optional)
    """

    def __init__(self, api_key:str, base_site:str='droplink.co'):
        self.__api_key = api_key
        self.__base_site = base_site
        self.__api_par = "api"
        self.__url_par = "url"
        self.__jsonpar = "shortenedUrl"
        self.qlink_par = "https://{base_site}/st?api={api_key}&url={url}"
        self.__base_url = f"https://{self.__base_site}/api"
        self.mime_type = "application/json"

        if self.__base_site == 'shareus.in':
            self.__base_url = f"https://api.{self.__base_site}/shortLink"
            self.__api_par = "token"
            self.__url_par = "link"
            self.__jsonpar = "shortlink"
            self.qlink_par = "https://api.{base_site}/directLink?token={api_key}&link={url}"
            self.mime_type = "text/html"


        if not self.__api_key:
            raise Exception("API key not provided")

    async def __fetch(self, session:aiohttp.ClientSession, params:dict) -> dict:
        """
        It takes a URL, a session, and a dictionary of parameters, and returns a JSON object
        
        :param url: The URL of the API endpoint we're requesting
        :param session: the aiohttp session object
        :param params: The parameters to pass to the API
        :return: A list of dictionaries.
        """
        async with session.get(self.__base_url, params=params, raise_for_status=True, ssl=False) as response:
            result = await response.json(content_type=self.mime_type) 
            return result

    async def convert(
        self, 
        link:str, 
        alias:str='',
        silently_fail:bool = False, 
        quick_link:bool = False,) -> str:
        """
        It converts a link to a short link.
        
        :param link: The link you want to shorten
        :type link: str

        :param alias: The alias you want to use for the link
        :type alias: str

        :param silently_fail: If this is set to True, then instead of raising an exception, it will return
        the original link, defaults to False
        :type silently_fail: bool (optional)

        :param quick_link: If you want to get a quick link, set this to True, defaults to False
        :type quick_link: bool (optional)
        
        :return: The shortened link is being returned.
        """

        is_short_link = await self.is_short_link(link)

        if is_short_link:
            return link
        if quick_link:
            return await self.get_quick_link(url=link)

        params = {
            self.__api_par: self.__api_key,
            self.__url_par : link,
            'alias': alias,
            'format':'json'
                }
        try:
            my_conn = aiohttp.TCPConnector(limit=10)
            async with aiohttp.ClientSession(connector=my_conn) as session:
                session = session
                data = await self.__fetch(session, params)

                if data["status"] == "success":
                    return data[self.__jsonpar]
                raise Exception(data['message'])
                
        except Exception as e:
            raise Exception(e)

    async def get_quick_link(self, url:str, **kwargs) -> str:
        """
        It returns the quick link for a given link
        
        :param urls: A list of urls to convert
        :alias: The alias to use for the link
        :return: The converted links.
        """
        return self.qlink_par.format(base_site=self.__base_site, api_key=self.__api_key, url=url)


    async def bulk_convert(self, urls:list, silently_fail:bool=True, quick_link:bool=False, **kwargs) -> list:
        """
        It converts a list of URLs to a list of shortened URLs.
        
        :param urls: A list of urls to convert
        :type urls: list
        :param silently_fail: If True, the function will return the given link instead of raising an exception, only if the function raise an exception,
        defaults to True
        :return: A list of the converted links.
        """

        tasks = []
        for url in urls:
            task = asyncio.ensure_future(self.convert(
                link=url, 
                silently_fail=silently_fail, 
                quick_link=quick_link))
            tasks.append(task)

        return await asyncio.gather(*tasks, return_exceptions=True)


    async def convert_from_text(self, text:str, silently_fail:bool=True, quick_link:bool=False) -> str:
        """
        It takes a string, finds all the links in it, converts them, and then replaces the original links
        with the converted ones
        
        :param text: The text to be converted
        :type text: str
        :param silently_fail: If True, the function will return the given link instead of raising an exception, only if the function raise an exception,
        defaults to True
        :return: A text of converted links
        """
        links = await self.__extract_url(text)
        converted_links = await self.bulk_convert(links, silently_fail=silently_fail, quick_link=quick_link)

        for i, droplink_link in enumerate(converted_links):
            text = text.replace(links[i], droplink_link)
        return text


    async def is_short_link(self, link:str) -> bool:
        """
        It checks if the link is a valid mdisk link.
        
        :param link: The link to the file
        :type link: str
        :return: True if the link is a valid mdisk link, False otherwise
        """
        domain = urlparse(link).netloc
        return self.__base_site in domain


    async def __extract_url(self, string:str) -> list:
        regex = r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))"""
        urls = re.findall(regex, string)
        return ["".join(x) for x in urls]

    @staticmethod
    def available_websites():
        available_websites = ["droplink.co", "gplinks.in" ,"tnlink.in", "za.gl" ,"du-link.in", "viplink.in", "shorturllink.in", "shareus.in", "All droplink.co Alternative Websites"]
        return "\n".join(available_websites)

